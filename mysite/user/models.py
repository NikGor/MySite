from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    job_title = models.CharField(max_length=100, null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    is_relocatable = models.BooleanField(default=False)
    linkedin = models.CharField(max_length=200, null=True, blank=True)
    about_me = models.TextField(null=True, blank=True)
