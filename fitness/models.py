from django.db import models

class Account(models.Model):
    username = models.CharField(max_length=30, blank=False, default='')
    first_name = models.CharField(max_length=30, blank=False, default='')

class Activity(models.Model):
    activity_name = models.CharField(max_length=30, blank=False, default='')