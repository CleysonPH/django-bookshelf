from django.urls import path
from django.contrib.auth.views import LogoutView

from .views import LoginView, PasswordChangeDoneView, PasswordChangeView, RegisterView, UserDetailView, profile_update


app_name = 'accounts'
urlpatterns = [
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('registro', RegisterView.as_view(), name='register'),
    path('atualizar/senha', PasswordChangeView.as_view(), name='password-change'),
    path('atualizar/senha/concluido',
         PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('atualizar/perfil', profile_update, name='profile-update'),
    path('<str:username>', UserDetailView.as_view(), name='user-detail'),
]
