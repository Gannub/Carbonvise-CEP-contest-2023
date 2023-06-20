from typing import Any
from django import http
from django.http.response import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from market.models import Market

class DealOwnerMixin(LoginRequiredMixin):

    def dispatch(self, request, *args, **kwargs):
        
        deal = Market.objects.get(slug=kwargs['slug'])
        if deal.dealer != request.user:
            return redirect('error403')

        if not request.user.is_authenticated:
            return self.handle_no_permission()

        return super().dispatch(request, *args, **kwargs)