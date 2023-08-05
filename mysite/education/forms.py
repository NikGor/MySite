from django import forms
from .models import Education


class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['school', 'faculty', 'start_date', 'end_date', 'description']
