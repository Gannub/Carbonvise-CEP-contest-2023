from typing import Any, Dict
from django.views.generic import TemplateView,ListView
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
        
        # user.make_dealer()
        print(ctx)
        return ctx

class UserListView(ListView):
    model = User
    template_name = 'user_list.html'
    def get_context_data(self,*args, **kwargs):
        ctx = super().get_context_data(*args , **kwargs)
        ctx['user_list'] = User.objects.all()
        
        return ctx