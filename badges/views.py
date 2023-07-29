
# Create your views here.
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView, FormView
from profiles.models import Profile,CreditSession, CreditHistory, Achievement
from carts.models import CartItemHistory
# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from badges.models import NeutralBadges, ArchiveNeutralBadge , AchievementBadges
from datetime import timedelta
from django.utils import timezone
import math
import json
from badges.imagemani import customBadge1
from django.contrib.auth.decorators import login_required




def ach_upload_path(str, time):
    return f'ach_badges/{str}/{time}.jpg'

@login_required
def obtainAchi(request, name):
    try: 
        # print(name)
        # profile_credit = CreditSession.objects.get(user=request.user)
        profile_achieve = CreditSession.objects.filter(user=request.user, achievements__name=name)
        # print(profile_achieve.exists())
        ach_, created = Achievement.objects.get_or_create(name=name)
        # print('hello')
        # print(ach_)
        if profile_achieve.exists():
            
                profile_credit = CreditSession.objects.get(user=request.user) 
                try:

                    ach_badges= AchievementBadges.objects.filter(in_session=profile_credit,in_achievement=ach_)
                    # profile_achieve
                    print(ach_badges)
                    if not ach_badges:
                        raise IndexError
                    
                    

                    else:
                        slug = ach_badges[0].slug   
                        print(slug)
                        ctx = {
                            'ach_slug':slug
                        } 
                        return render(request ,'badges/already_own_ach.html', ctx)
                
                    
                    
                    
                except:
                    ach_badges = AchievementBadges.objects.create(in_session=profile_credit,in_achievement=ach_)

                    badge_url = "static/img/design4.jpg" 

                    ach_badges.badges.save(ach_upload_path(str(profile_credit.session_name), str(profile_credit.start_date)), open(badge_url, 'rb'), save=True)
                    
                    ach_badges.session_name = profile_credit.session_name
                    
                    ach_badges.is_obtained = True
                    ach_badges.save()
                    
            
                    
                ctx = {
                        'ach_badge':ach_badges
                    }
                
                
                # print('pass test')
                return render(request, 'badges/obtain_ach_badge.html', ctx)
            # print(profile_achieve)
        # profile_credit.achievements
        
    except:
        
    
    
        return redirect('index')









def obtainBadges(request):

    # if request\
    if request.user.is_authenticated:
        try:
            profile_credit = CreditSession.objects.get(user=request.user)

            if profile_credit.is_neutral:
                
                if request.method == 'POST':
                    
                    number = int(request.POST.get('selected_number'))
                
                    


                    return redirect('badges:your_badge', number=number)
                    
                

            else:
                return HttpResponse('not neutral')
                

        
            return render(request, 'badges/obtain_badges.html')
        
        
        
        except:
            
            return redirect('howto')





# @login_required
# def badgesSelect(request):
#     data = json.loads(request.body)
#     #  print(data)
#     badge_choice = data['num']
#     print(badge_choice)

#     yourBadge(request, badge_choice)

#     return HttpResponse('nice')


    

# @login_required
# def badgesSelect(request):
#     if request.method == 'POST':
#         number = int(request.POST.get('selected'))
#         print(number)
#         return redirect('your_badge', number=number)
#     return HttpResponse('nice')
def get_image_url(image_number):
    image_urls = {
        1: "static/img/badges_test.png",
        2: "static/img/design1.jpg",
        3: "static/img/design2.jpg",
        4: "static/img/design3.jpg",
        5: "static/img/design4.jpg"
    }
    if 1 <= image_number <= 5:
        return image_urls[image_number]
    else:
        return None
    
def upload_path(str, time):
    return f'badges/{str}/{time}.jpg'
@login_required
def yourBadge(request, number):
    try:
        profile_credit = CreditSession.objects.get(user=request.user)
        badge, created = NeutralBadges.objects.get_or_create(in_session=profile_credit)

        if profile_credit.is_neutral:
            
            if not badge.is_obtained:
                
                # badge_url = get_image_url(number)
                
                badge, created = NeutralBadges.objects.get_or_create(in_session=profile_credit)
                badge_url = customBadge1(profile_credit.session_name, request.user)


                badge.badges.save(upload_path(str(profile_credit.session_name), str(profile_credit.start_date)), open(badge_url, 'rb'), save=True)
                badge.session_name = profile_credit.session_name
                badge.slug = profile_credit.slug
                badge.is_obtained = True
                badge.save()

                ctx = {
                    'badge_obj':badge
                }
                
                return render(request, 'badges/badges.html', ctx)
            else:
                return redirect('index')
        else:
            return HttpResponse('not neutral')#might change

        
    except:
        return redirect('index')

    
    
    
@login_required
def sessionBadgeView(request, slug):
    pass

class BadgeDetailView(DetailView):
    model = NeutralBadges

    template_name = 'badges/badge_view.html'

class AchBadgeDetailView(DetailView):
    model = AchievementBadges

    template_name = 'badges/ach_badge_view.html'
     