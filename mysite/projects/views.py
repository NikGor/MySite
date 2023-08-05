from .models import Project
from .forms import ProjectForm
from mysite.core.views import BaseListView, BaseCreateView, BaseUpdateView, BaseDeleteView


class ProjectListView(BaseListView):
    model = Project
    template_name = 'projects/project_list.html'
    context_object_name = 'projects'


class ProjectCreateView(BaseCreateView):
    model = Project
    form_class = ProjectForm
    template_name = 'projects/project_create.html'


class ProjectUpdateView(BaseUpdateView):
    model = Project
    form_class = ProjectForm
    template_name = 'projects/project_update.html'


class ProjectDeleteView(BaseDeleteView):
    model = Project
    template_name = 'projects/project_delete.html'
