from django.db import models
from django import forms

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    email_id = models.EmailField(max_length=30)
    ph_num = models.IntegerField()
    username = models.CharField(max_length=20)
    profile_pic = models.TextField()
    location = models.CharField(max_length=30)
    gender = models.CharField(max_length=2)
    dob = models.DateField()
    verified = models.IntegerField()


class Song(models.Model):
    audio_url = models.TextField()
    genre = models.CharField(max_length=20)
    duration = models.TimeField()
    release_date = models.DateField()
    language = models.CharField(max_length=10)
    title = models.TextField()

    user_id = models.ForeignKey(User)

