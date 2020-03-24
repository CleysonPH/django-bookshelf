from django.urls import path, reverse

from .views import LoginView, RegisterView


app_name = 'accounts'
urlpatterns = [
    path('login', LoginView.as_view(), name='login'),
    path('registro', RegisterView.as_view(), name='register'),
]
