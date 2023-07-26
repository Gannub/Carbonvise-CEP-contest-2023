from django.urls import path, include
from badges import views

app_name = 'badges'

urlpatterns = [
    path('obtain/', views.obtainBadges, name='obtain_badges'),
    # path('obtain/select', views.badgesSelect, name='badges_select'), #for javascript   
    path('yourbadge/<int:number>', views.yourBadge, name='your_badge'), 
    path('sessionbadge/<slug:slug>', views.BadgeDetailView.as_view(), name='badge_detail'),
   
 
]