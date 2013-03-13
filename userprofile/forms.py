from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User

__author__ = 'ir4y'


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User