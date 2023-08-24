from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'job_title', 'location', 'is_relocatable', 'linkedin', 'about_me']
