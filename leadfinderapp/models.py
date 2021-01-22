from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
# Create your models here.


class Emails(models.Model):
    name = models.CharField(max_length=40000)
    urls = models.URLField(max_length=200)
    emails = models.TextField()

    def __str__(self):
        return self.name



class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    avatar = models.ImageField(upload_to = "avatars/", null=True, blank=True)
