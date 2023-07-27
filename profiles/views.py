from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView, FormView
from profiles.models import Profile,CreditSession, CreditHistory
from carts.models import CartItemHistory
# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from profiles.forms import ProfileForm, SessionForm
from dealer.forms import DealerCreationForm
from datetime import timedelta
from django.utils import timezone
import math
from django.db.models import Sum, F, Window,Count, Q
from django.db.models.functions import Rank, DenseRank, Coalesce



from django.contrib.auth import get_user_model
User = get_user_model()
#Fatal: Add the Profile owner mixins here!!!! (later)
# class ProfileDetailView(DetailView):
    # model = Profile
    #make separate profile page 

# I am trying to use Function based views to make a separate profile page
# done!
def get_province_rank(user):
    # Calculate the total credits for each province
    provinces_credits_sum = (
        User.objects
        .values('province')
        .annotate(  total_credits=Coalesce(Sum('profile_credit__credits'), 0),
                    total_neutral=Count('id', filter=Q(profile_credit__is_neutral=True))
                  
        )
        .order_by('-total_neutral')
    )
    # print()
    # Calculate the rank of each province based on total credits
    # province_rank = provinces_credits_sum.annotate(rank=Window(expression=DenseRank(), order_by=F('total_neutral').desc()))
    # print(provinces_credits_sum)
    # user_province_rank = next((item['rank'] for item in province_rank if item['province'] == user.province), None)
    for rank, province in enumerate(provinces_credits_sum):
        if province['province']==user.province:
            # print(rank+1, province['province'])
            
            return rank+1

    
    # context = {
    #     'province_ranks': province_ranks
    # }
def get_user_rank(user):
    # Retrieve all users ordered by credits in descending order
    users = User.objects.select_related('profile_credit').order_by('-profile_credit__credits')
    # print(users)

    # Calculate the rank of the given user
    rank = 1
    for i, u in enumerate(users):
        if u == user:
            return rank
        rank+=1

    # If the user is not found in the leaderboard, return None
    return None
def get_user_province_rank(user):
    # Calculate the total credits for each province
    
    province_credits = User.objects.filter(province=user.province).annotate(total_credits=Sum('profile_credit__credits'))
    # print(province_credits)
    # Calculate the rank of the user's province based on total credits
    province_ranks = province_credits.annotate(rank=Window(expression=DenseRank(), order_by=F('total_credits').desc()))
    # print(province_ranks)
    # Get the rank of the user's province
    user_province_rank = province_ranks.filter(province=user.province).values_list('rank', flat=True).first()
    # print(user_province_rank, user.province)
    return user_province_rank


    context = {
        'province_rank': province_rank
    }

def profile_page(request, slug):
    if request.user.is_authenticated:
        profile = Profile.objects.get(slug=slug)

        try:      
            profile_credits = profile.user.profile_credit
            percentage = math.ceil(profile_credits.credits/10)
            user_rank = get_user_rank(profile.user)
            user_province_rank = get_user_province_rank(profile.user)
            province_rank = get_province_rank(profile.user)
            # print(request.user)
                # purchased_item = get_object_or_404(CartItemHistory, user=profile.user)
                # print(purchased_item, 'no way??')
                # if purchased_item.DoesNotExist:
                    # purchased_item = None
        except :
           #might fix this part later 
            user_rank = 'ไม่มีอันดับ'
            user_province_rank = 'ไม่มีอันดับ'
            province_rank =  get_province_rank(profile.user)
            profile_credits = None
            percentage = 0
        if profile.user==request.user:

            purchased_item = CartItemHistory.objects.filter(user=profile.user)
            session_history = CreditHistory.objects.filter(user=profile.user)

            
        else:
            purchased_item = None
    else:
        return redirect('account_login')
    
    ctx = {'req_profile':profile, 
           'credit_percentage':percentage,
           'profile_credit':profile_credits,
           'purchased_item':purchased_item, 
           'session_history':session_history,
           'user_rank':user_rank,
           'user_province_rank': user_province_rank,
           'province_rank': province_rank
           
    }

    return render (request,'profiles/profile_detail.html',ctx)

# def dealersignup_page(request):
#     req_slug = request.user.profile.slug
#     req_profile = get_object_or_404(Profile,slug=req_slug)
    
#     if request.method == 'POST':

#         form = DealerCreationForm(request.POST, instance=req_profile)

#         if form.is_valid():
            
#             dealer_form = form.save(commit=False)
            
#             print(dealer_form.image,'test')

#             dealer_form.save() #add to the database
#             return redirect('index')

#     else: 
#         form = DealerCreationForm(instance=req_profile)
#     print("im here")
    
#     return render (request,'profiles/sign_up_dealer.html', {'form':form})

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'profiles/profile_form.html'
    model = User

    form_class = ProfileForm

@login_required
def ProfileFirstCreate(request, slug):

    pass

class DealerForm(LoginRequiredMixin, CreateView):
    template_name = 'profiles/dealer_form.html'
    model = Profile

    form_class = DealerCreationForm
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)



#separate the function here later

#time schedule system (reset_credit.py)
def start_session(request, name , desc):
    # Get the user's credit information or create a new record if it doesn't exist
    
        user_session, created = CreditSession.objects.get_or_create(user=request.user)
        # print("check this line")
        if user_session.session_active:
            # print('check session active')
            # Check if the user has a credit reset date or if it's time to reset the credits
            if user_session.reset_date is None or user_session.reset_date <= timezone.now():
                # print('Test timelapse')
                # Store the current credits in the credit history
                if user_session.credits > 0:
                    CreditHistory.objects.create(
                        user=request.user, session_name=user_session.session_name, 
                        session_des=user_session.session_des,credits_of_month=user_session.credits,
                        start_date=user_session.start_date,end_date=timezone.now(),
                        slug=user_session.slug,
                        )

                # Reset the user's credits and set the new credit reset date to 1 month from now
                user_session.credits = 0
                user_session.start_date = timezone.now()
                user_session.reset_date = timezone.now() + timedelta(days=30)
                user_session.session_active = True #just to make sure
                user_session.save()
                # print('session created')
                return (user_session)
            
            
            # return render(request, 'profiles/session_page.html', {'session_status':2})

        else: # if user_session in inactive (it is inactive by default)
            # print('check inactive')
            user_session.credits = 0
            user_session.session_name = name
            user_session.session_des = desc
            user_session.start_date = timezone.now()
            user_session.reset_date = timezone.now() + timedelta(days=30)
            user_session.session_active = True #just to make sure
            user_session.save()

        
def end_session(request):
    # try : 
        user_session = CreditSession.objects.get(user=request.user)

        if user_session.credits > 0:
            #if user.isneutral we should collect badges in that session of that users
            CreditHistory.objects.create(user=request.user, session_name=user_session.session_name, session_des=user_session.session_des,credits_of_month=user_session.credits,start_date=user_session.start_date,end_date=timezone.now(),is_neutral=user_session.is_neutral,slug=user_session.slug)
        # print('pre _ delete')
        user_session.delete()
        
    # except:
        # pass
    

def endSessionView(request, slug):
    
    if request.user.is_authenticated:
        if request.method == 'POST':

            end_session(request)
            return redirect('index')
    else:
        return redirect('account_login')
    
    return render(request, 'profiles/end_session.html')



def sessionView(request, slug):

    user_session, created = CreditSession.objects.get_or_create(user=request.user)
 
    if request.user.is_authenticated:
    #  if not request.user.profile_credit.DoesNotExist:
        if not request.user.profile_credit.session_active:
            if request.method == 'POST':
                form =  SessionForm(request.POST)
 
                name = form.data['name']
                desc = form.data['description']
                print(name,desc)
                user_session = start_session(request, name, desc)
                    
                return redirect('index')
                
            else:
                form = SessionForm()
                
        else:

            
            return HttpResponse('session is already active')
    else:
        return redirect('account_login')
    
    
    if request.user.is_authenticated:
        profile_slug = Profile.objects.get(slug=slug) 
    
    # ctx = { 'session_start': user_session.start_date,
    #         'session_end': user_session.reset_date,
    #         'session_status': user_session.session_active,
    #         'profile_slug':profile_slug
    # }
    return render(request, 'profiles/session_page.html', {"form": form})


def makeNeutral():
    pass

