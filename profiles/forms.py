from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from profiles.models import Profile
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit
User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        exclude = []
        fields = ['first_name','last_name','username','email',]

class DealerCreationForm(forms.ModelForm):

    class Meta:
        model = Profile 
        exclude = []
        fields = ['province','about_me','image']    

