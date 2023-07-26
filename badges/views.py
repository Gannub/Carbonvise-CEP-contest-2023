
# Create your views here.
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView, FormView
from profiles.models import Profile,CreditSession, CreditHistory
from carts.models import CartItemHistory
# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from badges.models import NeutralBadges, ArchiveNeutralBadge
from datetime import timedelta
from django.utils import timezone
import math
import json


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
        2: "static/img/badge2.jpg",
        3: "static/img/badge3.png",
        4: "static/img/badge4.png",
        5: "static/img/badge5.png"
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
                
                badge_url = get_image_url(number)

                badge, created = NeutralBadges.objects.get_or_create(in_session=profile_credit)
                
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
    