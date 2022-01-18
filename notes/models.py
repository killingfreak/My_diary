from django.db import models
from django.conf import settings
# Create your models here.

User = settings.AUTH_USER_MODEL


class Registration(models.Model):
    user_name = models.CharField(max_length=30)
    mobile = models.PositiveIntegerField()
    email = models.EmailField()
    password = models.CharField(max_length=15)

class Note(models.Model):
    user = models.ForeignKey(User, default = 1, null=True , on_delete= models.SET_NULL)
    subject = models.TextField()
    text = models.TextField()
    date = models.DateTimeField(auto_now=True)

