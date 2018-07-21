from django.contrib.auth.models import User
from django.db import models
from tinymce.models import HTMLField

# Create your models here.


class Profile(models.Model):
    profile_photo = models.ImageField(upload_to = 'profpic/')
    bio = models.TextField(max_length=100)
    insta_user = models.ForeignKey(User)

    def __str__(self):
        return self.insta_user


class Image(models.Model):
    image = models.ImageField(upload_to = 'images/')
    image_name = models.CharField(max_length=30)
    image_caption = models.TextField(max_length=100)
    profile = models.ForeignKey(Profile)

    def __str__(self):
        self.image_name
