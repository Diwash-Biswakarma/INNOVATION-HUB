from django.db import models
from django.urls import reverse
from django.conf import settings
from datetime import datetime

PROVINCES = [
    ('1', 'State 1'),
    ('2', 'State 2'),
    ('3', 'State 3'),
    ('4', 'State 4'),
    ('5', 'State 5'),
    ('6', 'State 6'),
    ('7', 'State 7'),
]

GENDER = [
    ('F', 'Female'),
    ('M', 'Male'),
    ('O', 'Other'),
]


class Work(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    age = models.IntegerField()
    gender = models.CharField(max_length=1, choices=GENDER)
    letter = models.TextField(max_length=5000, default=None)
    cv = models.FileField(max_length=250, default=1)

    def __str__(self):
        return self.name


class Blog(models.Model):
    blog_name = models.CharField(max_length=200, default=1)
    blog_writer = models.CharField(max_length=100, default=None)
    blog = models.TextField(max_length=1000, default=None)


class Message(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=150)
    message = models.TextField(max_length=250)


class Apply(models.Model):
    job = models.TextField(max_length=100)
    qualification = models.CharField(max_length=100)
    deadline = models.CharField(max_length=100)
    description = models.TextField(max_length=250)


class Media(models.Model):
    title = models.CharField(max_length=100, default=None)
    description = models.TextField(max_length=1000, default=None)
