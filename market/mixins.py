from typing import Any
from django import http
from django.http.response import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from market.models import Market
from django.contrib.auth import get_user_model

User = get_user_model()

class DealOwnerMixin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        
        deal = Market.objects.get(slug=kwargs['slug'])
        if deal.dealer != request.user:
            return redirect('error403')

        if not request.user.is_authenticated:
            return self.handle_no_permission()

        return super().dispatch(request, *args, **kwargs)
    


class IsDealerMixin(LoginRequiredMixin):   
      def dispatch(self, request, *args, **kwargs):
        
        user = User.objects.get(username=request.user)

        if not user.is_dealer:
            return redirect('error403')

        if not request.user.is_authenticated:
            return self.handle_no_permission()

        return super().dispatch(request, *args, **kwargs)