from django.urls import path, include
from market import views

app_name = 'market'

urlpatterns = [
    path('', views.MarketListView.as_view(), name='market_list'),
    path('detail/<slug:slug>', views.MarketDetailView.as_view(), name='market_detail')

]