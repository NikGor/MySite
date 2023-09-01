from django.db import models


class JobApplication(models.Model):
    id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=255, blank=True, null=True)
    job_title = models.CharField(max_length=255)
    url = models.URLField()
    location = models.CharField(max_length=255)
    date_added = models.DateTimeField(auto_now_add=True)
    responded = models.BooleanField(default=False)
    cover_letter = models.TextField(blank=True, null=True)
    response_received = models.BooleanField(default=False)
    phone_interview_invited = models.BooleanField(default=False)
    phone_interview_date = models.DateTimeField(null=True, blank=True)
    phone_interview_done = models.BooleanField(default=False)
    onsite_interview_invited = models.BooleanField(default=False)
    onsite_interview_date = models.DateTimeField(null=True, blank=True)
    onsite_interview_done = models.BooleanField(default=False)
    contact_person = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(
        max_length=50,
        choices=[('pending', 'Pending'), ('accepted', 'Accepted'), ('rejected', 'Rejected')],
        default='pending'
    )
    salary_range = models.CharField(max_length=100, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    final_decision = models.CharField(
        max_length=50,
        choices=[('accepted', 'Accepted'), ('rejected', 'Rejected')],
        blank=True, null=True
    )
