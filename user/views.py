from django.shortcuts import redirect, get_object_or_404
from django.views.generic.edit import FormView
from .models import User
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.utils.translation import gettext as _
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from .forms import UserUpdateForm

User = get_user_model()


class UserView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = 'user/user_profile.html'
    success_url = reverse_lazy('index')

    def get_object(self, queryset=None):
        return self.request.user


class UpdateUserView(LoginRequiredMixin, FormView):
    form_class = UserUpdateForm
    template_name = 'user/user_profile.html'
    success_url = reverse_lazy('user:user')

    def dispatch(self, request, *args, **kwargs):
        self.object = get_object_or_404(User, pk=self.kwargs['pk'])
        if self.request.user == self.object:
            return super().dispatch(request, *args, **kwargs)
        else:
            messages.error(self.request, _("У вас нет прав для изменения другого пользователя."))
            return redirect('user:user')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'instance': self.object})
        return kwargs

    def form_valid(self, form):
        form.save()
        messages.success(self.request, _("Пользователь успешно изменен"))
        update_session_auth_hash(self.request, form.instance)
        return super().form_valid(form)

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, f"{field}: {error}")
        return self.render_to_response(self.get_context_data(form=form))
