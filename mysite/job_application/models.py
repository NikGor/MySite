from ckeditor.fields import RichTextField
from django.db import models


class JobApplication(models.Model):
    id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=255, blank=True, null=True)
    job_title = models.CharField(max_length=255, blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    is_remote = models.BooleanField(default=False, blank=True, null=True)
    key_skills = models.TextField(blank=True, null=True)
    soft_skills = models.TextField(blank=True, null=True)
    language = models.CharField(max_length=10, blank=True, null=True)
    german_level = models.CharField(max_length=255, blank=True, null=True)
    required_experience = models.CharField(max_length=255, blank=True, null=True)
    minuses = models.TextField(max_length=255, blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    cover_letter = models.TextField(blank=True, null=True)
    cv_intro = RichTextField(blank=True, null=True)
    response_received = models.BooleanField(default=False)
    phone_interview_date = models.DateTimeField(null=True, blank=True)
    onsite_interview_date = models.DateTimeField(null=True, blank=True)
    contact_person = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(
        max_length=50,
        choices=[('pending', 'Pending'), ('accepted', 'Accepted'), ('rejected', 'Rejected')],
        default='pending'
    )
    salary_range = models.CharField(max_length=255, blank=True, null=True)
    vacation_days = models.CharField(max_length=255, blank=True, null=True)
    other_benefits = models.TextField(max_length=512, blank=True, null=True)
    info = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
