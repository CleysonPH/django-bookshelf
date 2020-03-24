from django.contrib.auth.views import LoginView as GenericLoginView


class LoginView(GenericLoginView):
    template_name = 'accounts/login.html'

    def get_context_data(self, **kwargs):
        context = super(LoginView, self).get_context_data(**kwargs)
        context['page_title'] = 'Login'
        context['page_description'] = 'Faça o login na plataforma e tenha acesso a todos os recursos'
        return context
