from .models import Experience
from .forms import ExperienceForm
from mysite.core.views import BaseListView, BaseCreateView, BaseUpdateView, BaseDeleteView


class ExperienceListView(BaseListView):
    model = Experience
    template_name = 'experience/experience_list.html'
    context_object_name = 'experiences'


class ExperienceCreateView(BaseCreateView):
    model = Experience
    form_class = ExperienceForm
    template_name = 'experience/experience_create.html'


class ExperienceUpdateView(BaseUpdateView):
    model = Experience
    form_class = ExperienceForm
    template_name = 'experience/experience_update.html'


class ExperienceDeleteView(BaseDeleteView):
    model = Experience
    template_name = 'experience/experience_delete.html'
