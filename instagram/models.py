from django.contrib.auth.models import User
from django.db import models
from tinymce.models import HTMLField

# Create your models here.


class Profile(models.Model):
    profile_photo = models.ImageField(upload_to = 'profpic/')
    bio = models.TextField(max_length=100)
    user = models.ForeignKey(User)

    def __str__(self):
        return self.insta_user

    def profile_save(self):
        self.save()


class Image(models.Model):
    image = models.ImageField(upload_to = 'images/')
    image_name = models.CharField(max_length=30)
    image_caption = models.TextField(blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)


    def __str__(self):
        self.image_name

    def save_images(self):
        self.save()