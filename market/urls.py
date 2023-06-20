from django.urls import path, include
from market import views

app_name = 'market'

urlpatterns = [
    path('', views.MarketListView.as_view(), name='market_list'),
    path('detail/<slug:slug>', views.MarketDetailView.as_view(), name='market_detail'),
    path('create', views.MarketCreateView.as_view(), name='market_create'),
    path('update/<slug:slug>', views.MarketUpdateView.as_view(), name='market_update'),
    path('delete/<slug:slug>', views.MarketDeleteView.as_view(), name='market_delete'),
 
]