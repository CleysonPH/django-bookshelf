from django.contrib.auth.forms import UserCreationForm as DefaultUserCreationForm
from django.contrib.auth.models import User


class UserCreationForm(DefaultUserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
