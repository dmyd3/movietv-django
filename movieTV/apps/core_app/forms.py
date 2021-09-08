from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _
from core_app.models import User

class RegisterForm(UserCreationForm):

    # first_name = forms.CharField(label=_('first name'), max_length=50)
    # last_name = forms.CharField(label=_('last name'), max_length=50)
    
    class Meta:
        model = User
        fields = ["username", "password1", "password2", "email",
            "first_name", "last_name"]