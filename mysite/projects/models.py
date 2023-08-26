from django.db import models
from mysite.user.forms import User


class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200)
    github_url = models.URLField(null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    description = models.TextField()
    screenshot_url = models.TextField(null=True, blank=True)
