from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'birth_date', 'job_title',
                  'location', 'is_relocatable',
                  'linkedin', 'phone_number', 'about_me']
