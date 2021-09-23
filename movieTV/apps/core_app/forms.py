from django import forms
import os

from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.forms import widgets
from django.utils.translation import gettext_lazy as _
from core_app.models import User

avatar_abs_path = os.path.join(settings.BASE_DIR,'movieTV/static/images/profile/')


class RegisterForm(UserCreationForm):

    # first_name = forms.CharField(label=_('first name'), max_length=50)
    # last_name = forms.CharField(label=_('last name'), max_length=50)
    custom_avatar_path = forms.FilePathField(path=avatar_abs_path)

    class Meta:
        model = User
        fields = ["username", "password1", "password2", "email",
            "first_name", "last_name", "custom_avatar_path"]
        