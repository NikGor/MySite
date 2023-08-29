from django.db import models
from mysite.user.models import User


class OpenSourceProject(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    job_title = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    start_date = models.CharField(max_length=100)
    end_date = models.CharField(max_length=100, null=True, blank=True)
    url = models.URLField()
    github_url = models.URLField()
    screenshot_url = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField()
