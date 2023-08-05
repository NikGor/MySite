from django.db import models
from mysite.user.forms import User


class Education(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    school = models.CharField(max_length=100)
    faculty = models.CharField(max_length=100)
    start_date = models.CharField(max_length=100)
    end_date = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField()
