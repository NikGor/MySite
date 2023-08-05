from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


class BaseListView(ListView):
    context_object_name = 'items'
    template_name = 'base/base_list.html'


class BaseCreateView(CreateView):
    template_name = 'base/base_create.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class BaseUpdateView(UpdateView):
    template_name = 'base/base_update.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class BaseDeleteView(DeleteView):
    template_name = 'base/base_delete.html'
    success_url = reverse_lazy('index')
