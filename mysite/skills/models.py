from django.db import models
from mysite.user.forms import User


class Skill(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    skill_type = models.CharField(max_length=100)
    description = models.TextField()
