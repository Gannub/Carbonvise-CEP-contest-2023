from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from dealer.models import Dealer
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit

User = get_user_model()
 
class DealerCreationForm(forms.ModelForm):

    class Meta:
        model = Dealer
        exclude = ['is_verify','user']
        # fields = []  
        labels = {
            'company_name' : 'Business Name',
            'shop_name' : 'Shop name (Shop profile)',
            'deal_province' : 'Province',
            'shop_icon' : 'Shop profile picture',
            'verify' : 'TGO certificate proof',

        }