from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from mysite.mixins import CustomLoginRequiredMixin


class BaseListView(CustomLoginRequiredMixin, ListView):
    context_object_name = 'items'
    template_name = 'base/base_list.html'


class BaseCreateView(CustomLoginRequiredMixin, CreateView):
    template_name = 'base/base_create.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class BaseUpdateView(CustomLoginRequiredMixin, UpdateView):
    template_name = 'base/base_update.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class BaseDeleteView(CustomLoginRequiredMixin, DeleteView):
    template_name = 'base/base_delete.html'
    success_url = reverse_lazy('index')
