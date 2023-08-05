from django import forms
from .models import Skill


class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['skill_type', 'description']