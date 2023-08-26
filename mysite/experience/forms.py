from django import forms
from .models import Experience


class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ['job_title', 'company', 'city', 'country', 'start_date', 'end_date', 'description']
