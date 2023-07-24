
from django.urls import path, include
from leaderboards import views

app_name = 'leaderboards'

urlpatterns = [
    # path('<slug:slug>', views.ProfileDetailView.as_view(), name='profile_detail'),
    path('', views.leaderboard_by_province, name='leaderboards'),
    path('user_by_credits', views.user_by_credits, name='user_by_credits'),
]