from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api import views
# from api.views import UserViewsets

app_name = 'api'

router = DefaultRouter()
# router.register('user',UserViewsets)  


urlpatterns = [
    path('', views.UserAPIView.as_view(), name='user_api'),
    # path('',include(router.urls)),

 
]