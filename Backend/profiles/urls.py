from django.urls import path, include
from profiles import views

app_name = 'profiles'

urlpatterns = [
    # path('<slug:slug>', views.ProfileDetailView.as_view(), name='profile_detail'),
    path('detail/<slug:slug>', views.profile_page, name='profile_page'),
    path('<slug:slug>/start_session', views.sessionView, name='start_session'),
    path('<slug:slug>/end_session', views.endSessionView, name='end_session'),
    # path('dealer_signup', views.dealersignup_page, name='dealer_signup'), 
    path('update/<slug:slug>', views.ProfileUpdateView.as_view(), name='profile_update'),
    path('<slug:slug>/become-dealer', views.DealerForm.as_view(), name='become_dealer'),
]