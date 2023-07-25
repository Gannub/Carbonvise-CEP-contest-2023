from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from profiles.models import Profile, CreditSession
# from crispy_forms.helper import FormHelper
# # from crispy_forms.layout import Layout, Fieldset, Submit
User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        exclude = []
        fields = ['first_name','last_name','username','email','province']

class ProfileForm(forms.ModelForm):

    class Meta:
        model = User 
        exclude = []
        fields = ['first_name','last_name','email','province']

class SessionForm(forms.Form):
     name = forms.CharField(label="Session name", max_length=100)
     description = forms.CharField(label='Descriptions or Oath', max_length=250)


