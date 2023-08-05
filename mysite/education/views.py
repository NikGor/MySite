from .models import Education
from .forms import EducationForm
from mysite.core.views import BaseListView, BaseCreateView, BaseUpdateView, BaseDeleteView


class EducationListView(BaseListView):
    model = Education
    template_name = 'education/education_list.html'
    context_object_name = 'educations'


class EducationCreateView(BaseCreateView):
    model = Education
    form_class = EducationForm
    template_name = 'education/education_create.html'


class EducationUpdateView(BaseUpdateView):
    model = Education
    form_class = EducationForm
    template_name = 'education/education_update.html'


class EducationDeleteView(BaseDeleteView):
    model = Education
    template_name = 'education/education_delete.html'
