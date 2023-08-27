from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy


class CustomLoginRequiredMixin(LoginRequiredMixin):
    """Require that the user is authenticated."""

    def handle_no_permission(self):
        return redirect(reverse_lazy('404'))
