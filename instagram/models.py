from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Profile(models.Model):
    profile_photo = models.ImageField(upload_to = 'profpic/')
    bio = models.TextField(max_length=100)
    insta_user = models.ForeignKey(User)
