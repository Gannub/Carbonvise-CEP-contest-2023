from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView, FormView
from profiles.models import Profile,CreditSession, CreditHistory
# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from profiles.forms import ProfileForm
from dealer.forms import DealerCreationForm
from datetime import timedelta
from django.utils import timezone
import math

#Fatal: Add the Profile owner mixins here!!!! (later)
# class ProfileDetailView(DetailView):
    # model = Profile
    #make separate profile page 

# I am trying to use Function based views to make a separate profile page


def profile_page(request, slug):
    if request.user.is_authenticated:
        profile = Profile.objects.get(slug=slug)
        try:      
            profile_credits = profile.user.profile_credit
            percentage = math.ceil(profile_credits.credits)

        except :
           #might fix this part later 
            percentage = 0


    else:
        return redirect('account_login')
    
    ctx = {'req_profile':profile, 'profile_credit':percentage}

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
    model = Profile

    form_class = ProfileForm

class DealerForm(LoginRequiredMixin, CreateView):
    template_name = 'profiles/dealer_form.html'
    model = Profile

    form_class = DealerCreationForm
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)




def start_session(request, slug):
    # Get the user's credit information or create a new record if it doesn't exist
    
    if request.user.is_authenticated:
        user_session, created = CreditSession.objects.get_or_create(user=request.user)
        # print("check this line")
        if user_session.session_active:
            print('check session active')
            # Check if the user has a credit reset date or if it's time to reset the credits
            if user_session.reset_date is None or user_session.reset_date <= timezone.now():
                print('Test timelapse')
                # Store the current credits in the credit history
                if user_session.credits > 0:
                    CreditHistory.objects.create(user=request.user, credits_of_month=user_session.credits,start_date=user_session.start_date,end_date=timezone.now())

                # Reset the user's credits and set the new credit reset date to 1 month from now
                user_session.credits = 0
                user_session.start_date = timezone.now()
                user_session.reset_date = timezone.now() + timedelta(days=30)
                user_session.session_active = True #just to make sure
                user_session.save()
                # print('session created')
            
            
            # return render(request, 'profiles/session_page.html', {'session_status':2})

        else: # if user_session in inactive (it is inactive by default)
            # print('check inactive')
            user_session.credits = 0
            user_session.start_date = timezone.now()
            user_session.reset_date = timezone.now() + timedelta(days=30)
            user_session.session_active = True #just to make sure
            user_session.save()

        

    else:
        return redirect('account_login')
    if request.user.is_authenticated:
        profile_slug = Profile.objects.get(slug=slug) 
    ctx = { 'session_start': user_session.start_date,
            'session_end': user_session.reset_date,
            'session_status': user_session.session_active,
            'profile_slug':profile_slug
    }
    return render(request, 'profiles/session_page.html', ctx)

