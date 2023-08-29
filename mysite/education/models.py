from django.db import models
from mysite.user.models import User


class Education(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    school = models.CharField(max_length=100)
    faculty = models.CharField(max_length=100)
    url = models.URLField(null=True, blank=True)
    start_date = models.CharField(max_length=100)
    end_date = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField()
