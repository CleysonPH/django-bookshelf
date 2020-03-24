from django.urls import reverse_lazy
from django.contrib.auth.views import (
    LoginView as GenericLoginView,
    PasswordChangeView as GenericPasswordChangeView,
    PasswordChangeDoneView as GenericPasswordChangeDoneView,
)
from django.contrib.auth.models import User
from django.views.generic import CreateView

from .forms import UserCreationForm


class LoginView(GenericLoginView):
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True

    def get_context_data(self, **kwargs):
        context = super(LoginView, self).get_context_data(**kwargs)
        context['page_title'] = 'Login'
        context['page_description'] = 'Faça o login na plataforma e tenha acesso a todos os recursos disponiveis'
        return context


class RegisterView(CreateView):
    template_name = 'accounts/register.html'
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accounts:login')

    def get_context_data(self, **kwargs):
        context = super(RegisterView, self).get_context_data(**kwargs)
        context['page_title'] = 'Registro'
        context['page_description'] = 'Faça o seu cadastro na plataforma e tenha acesso a todos os recursos disponiveis'
        return context


class PasswordChangeView(GenericPasswordChangeView):
    template_name = 'accounts/password_change_form.html'
    success_url = reverse_lazy('accounts:password_change_done')

    def get_context_data(self, **kwargs):
        context = super(PasswordChangeView, self).get_context_data(**kwargs)
        context['page_title'] = 'Atualizar Senha'
        context['page_description'] = 'Atualize a senha do seu registro aqui'
        return context


class PasswordChangeDoneView(GenericPasswordChangeDoneView):
    template_name = 'accounts/password_change_done.html'

    def get_context_data(self, **kwargs):
        context = super(PasswordChangeDoneView,
                        self).get_context_data(**kwargs)
        context['page_title'] = 'Operação concluida'
        context['page_description'] = 'Sua senha foi alterada com sucesso'
        return context
