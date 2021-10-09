from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
class OrderItem(models.Model):
    userId = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    image = models.URLField(default='')
    title = models.CharField(max_length=100, default='')
    quanity = models.IntegerField(default=1)


class OrderDetail(models.Model):
    userId = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    quanity = models.IntegerField(default=0)
    image = models.URLField(default='')
    title = models.CharField(max_length=100, default='')


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=100, default='')
    city = models.CharField(max_length=100,default='')
    website = models.URLField(default='')
    phone = models.IntegerField(default=0)

def create_profile(sender, **kawrgs):
    if kawrgs['created']:
        user_profile = UserProfile.objects.create(user=kawrgs['instance'])


class Book(models.Model):
    title = models.CharField(max_length=100, default='')
    author = models.CharField(max_length=100, default='')
    price = models.IntegerField(default=0)
    quanity = models.IntegerField(default=0)
    image = models.URLField(default='')

def create_book(sender, **kawrgs):
    if kawrgs['created']:
        book = Book.objects.create(user=kawrgs['instance'])


post_save.connect(create_profile, sender=User)
