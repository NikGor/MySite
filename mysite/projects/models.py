from django.db import models
from mysite.user.forms import User


class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200)
    url = models.URLField()
    description = models.TextField()
    screenshot_url = models.TextField(null=True, blank=True)
