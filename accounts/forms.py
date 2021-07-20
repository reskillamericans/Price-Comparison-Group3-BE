from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _

from .models import User


class RegisterForm(UserCreationForm):
    
    error_css_class = 'error'
    required_css_class = 'required'

    class Meta:
        model = User
        fields = ['username', 'email',
                  'first_name', 'last_name', 'password1']

