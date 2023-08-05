from .models import Skill
from .forms import SkillForm
from mysite.core.views import BaseListView, BaseCreateView, BaseUpdateView, BaseDeleteView


class SkillListView(BaseListView):
    model = Skill
    template_name = 'skills/skill_list.html'
    context_object_name = 'skills'


class SkillCreateView(BaseCreateView):
    model = Skill
    form_class = SkillForm
    template_name = 'skills/skill_create.html'


class SkillUpdateView(BaseUpdateView):
    model = Skill
    form_class = SkillForm
    template_name = 'skills/skill_update.html'


class SkillDeleteView(BaseDeleteView):
    model = Skill
    template_name = 'skills/skill_delete.html'
