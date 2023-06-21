from typing import Any, Dict
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from market.models import Market
from django.db.models import Count
from django.contrib.auth import get_user_model

User = get_user_model()

class BecomeADealerTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'become_a_dealer.html'

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)

        user = User.objects.get(username=self.request.user)
        
        user.make_dealer()
        print(ctx)
        return ctx
