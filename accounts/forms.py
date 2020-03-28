from django import forms
from django.contrib.auth.forms import UserCreationForm as DefaultUserCreationForm
from django.contrib.auth.models import User

from .models import UserProfile


class UserCreationForm(DefaultUserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class UserProfileModelForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)
