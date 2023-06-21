from typing import Any, Dict
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from market.mixins import DealOwnerMixin, IsDealerMixin
from market.models import Market
from market.forms import MarketForm
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model



User = get_user_model()

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
   
class MarketCreateView(IsDealerMixin, CreateView):
    model = Market
    form_class = MarketForm

    def form_valid(self, form ,*args, **kwargs):
        market = form.save(commit=False)

        dealer = User.objects.get(username = self.request.user)
        market.dealer = dealer
        market.save()
        return super().form_valid(form, *args,**kwargs)
    
class MarketUpdateView(DealOwnerMixin, UpdateView):
    model = Market
    form_class = MarketForm


class MarketDeleteView(DealOwnerMixin,DeleteView):
    model = Market
    success_url = reverse_lazy("market:market_list")
