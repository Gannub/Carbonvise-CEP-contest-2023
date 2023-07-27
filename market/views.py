from typing import Any, Dict
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView,DetailView,UpdateView
from market.models import Market
# Create your views here.
class MarketListView(ListView):
    model = Market
    # template_name = 'market_list'
    def get_context_data(self,*args, **kwargs):
        ctx = super().get_context_data(*args , **kwargs)
        ctx['market_list'] = Market.objects.all()
        
        return ctx

class MarketDetailView(DetailView):
    model = Market
    def get_context_data(self,*args, **kwargs):
        ctx = super().get_context_data(*args , **kwargs)
        ctx['deal_list'] = Market.objects.filter(category=ctx['market'].category)
        return ctx
   
