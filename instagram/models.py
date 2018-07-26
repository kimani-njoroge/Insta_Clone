from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Profile(models.Model):
    profile_photo = models.ImageField(upload_to = 'profpic/')
    bio = models.TextField(max_length=100)
    user = models.ForeignKey(User)
    insta_name = models.CharField(max_length=30)

    def __str__(self):
        return self.insta_name

    def profile_save(self):
        self.save()

    @classmethod
    def get_profs(cls):
        profile = cls.objects.all()
        return profile

    @classmethod
    def profile_search(cls, query):
        profile = cls.objects.filter(user__username__icontains=query)
        return profile


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

    @classmethod
    def get_images(cls):
        images = cls.objects.all()
        return images

class Comment(models.Model):
    user = models.ForeignKey(User)
    image = models.ForeignKey(Image)
    comment_text = models.CharField(max_length=100)