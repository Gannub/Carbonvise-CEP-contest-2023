"""
URL configuration for carbonvise project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView,ListView
from carbonvise import views,settings
# from carbonvise.views import BecomeADealerTemplateView
from django.conf import settings
from django.conf.urls.static import static
from carbonvise.views import UserListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('error403', TemplateView.as_view(template_name='error403.html'), name='error403'),
    path('success', TemplateView.as_view(template_name='success.html'), name='success'),

    path('howto', TemplateView.as_view(template_name='session_edu.html'), name='howto'),
    # path('become_a_dealer', views.BecomeADealerTemplateView.as_view(), name='become_a_dealer'),
    #market app
    path('market/', include('market.urls',namespace='market')),
    path('profile/', include('profiles.urls',namespace='profiles')),  
    path('cart/', include('carts.urls',namespace='cart')),
    #allauth
    path('accounts/', include('allauth.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('userlist',UserListView.as_view(), name='user_list'), 

    path('api/', include('api.urls',namespace='api')),
    path('leaderboards/', include('leaderboards.urls',namespace='leaderboards')),
    path('badges/', include('badges.urls',namespace='badges')),
    path('blogs/', include('blogs.urls',namespace='blogs')),
    path('billings/', include('billings.urls',namespace='billings')),

    
    


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

