from django.urls import path, include
from blogs import views

app_name = 'blogs'

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.blog, name='post_list'),# what does this link to? #it's the blog that has pages and maybe I would delete 'index'
    path('post/<slug:slug>/', views.post, name='post-detail')
    
]