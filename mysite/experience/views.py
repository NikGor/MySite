from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Experience
from .forms import ExperienceForm


class ExperienceListView(ListView):
    model = Experience
    template_name = 'experience/experience_list.html'
    context_object_name = 'experiences'


class ExperienceCreateView(CreateView):
    model = Experience
    form_class = ExperienceForm
    template_name = 'experience/experience_create.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ExperienceUpdateView(UpdateView):
    model = Experience
    form_class = ExperienceForm
    template_name = 'experience/experience_update.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ExperienceDeleteView(DeleteView):
    model = Experience
    template_name = 'experience/experience_delete.html'
    success_url = reverse_lazy('index')
