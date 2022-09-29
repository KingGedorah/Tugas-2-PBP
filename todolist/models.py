from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class Task (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,blank=True, null=True,)
    date = models.DateField(auto_now=True)
    title = models.TextField()
    description = models.TextField()
    is_finished = models.BooleanField(default=False)