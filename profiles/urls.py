from django.urls import path, include
from profiles import views

app_name = 'profiles'

urlpatterns = [
    # path('<slug:slug>', views.ProfileDetailView.as_view(), name='profile_detail'),
    path('detail/<slug:slug>', views.profile_page, name='profile_page'),
    # path('dealer_signup', views.dealersignup_page, name='dealer_signup'), 
    path('update/<slug:slug>', views.ProfileUpdateView.as_view(), name='profile_update'),
    path('update/<slug:slug>', views.ProfileUpdateView.as_view(), name='dealer_signup'),
]