from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.contrib.auth.views import (
    LoginView as GenericLoginView,
    PasswordChangeView as GenericPasswordChangeView,
    PasswordChangeDoneView as GenericPasswordChangeDoneView,
)
from django.views.generic import DetailView
from django.contrib.auth.models import User
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required

from .forms import UserCreationForm, UserUpdateForm, UserProfileModelForm
from .models import UserProfile


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

    def form_valid(self, form):
        self.object = form.save()
        UserProfile.objects.create(user=self.object)
        return super().form_valid(form)


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


class UserDetailView(DetailView):
    model = User
    template_name = 'accounts/user_detail.html'

    def get_context_data(self, **kwargs):
        context = super(UserDetailView, self).get_context_data(**kwargs)
        context['page_title'] = 'Perfil'
        context['page_description'] = f'Informações sobre o usuário {context["user"].get_full_name() or context["user"].username}'
        return context

    def get_object(self):
        return get_object_or_404(User, username=self.kwargs.get('username'))


@login_required
def profile_update(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        user_profile_form = UserProfileModelForm(
            request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and user_profile_form.is_valid():
            user_form.save()
            user_profile_form.save()

            return redirect('accounts:user-detail', username=request.user.username)

    user_form = UserUpdateForm(instance=request.user)
    user_profile_form = UserProfileModelForm(instance=request.user.profile)
    context = {
        'page_title': 'Atualizar Perfil',
        'page_description': f'Atualizar as informações sobre o usuário {request.user.get_full_name() or request.user.username}',
        'user_form': user_form,
        'user_profile_form': user_profile_form,
    }

    return render(request, 'accounts/profile_update.html', context)
