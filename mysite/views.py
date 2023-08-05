from django.shortcuts import render
from django.shortcuts import redirect
from django.views import View
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext as _
from django.contrib.auth import get_user_model


class IndexView(View):
    def get(self, request):
        profile_user = get_user_model().objects.first()
        experiences = profile_user.experience_set.all()
        educations = profile_user.education_set.all()
        return render(request, 'index.html', {'profile_user': profile_user,
                                              'experiences': experiences,
                                              'educations': educations})


# Create your views here.
class LoginView(FormView):
    form_class = AuthenticationForm
    template_name = 'user/login.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(self.request, user)
                messages.info(self.request, _("Вы залогинены"))
            else:
                messages.error(self.request, _("Этот аккаунт отключен."))
        else:
            messages.error(self.request, _("Неверное имя пользователя или пароль."))
        return super().form_valid(form)


class LogoutView(View):
    def get(self, request):
        logout(request)
        messages.success(request, _("Вы разлогинены"))
        return redirect('index')
