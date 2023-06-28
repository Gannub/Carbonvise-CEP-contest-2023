from django.urls import path, include
from profiles import views

app_name = 'profiles'

urlpatterns = [
    # path('<slug:slug>', views.ProfileDetailView.as_view(), name='profile_detail'),
    path('<slug:slug>', views.profile_page, name='profile_page'),
 
]