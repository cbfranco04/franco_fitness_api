from django.db import models


class Account(models.Model):
    username = models.CharField(max_length=30, blank=False, default="")
    first_name = models.CharField(max_length=30, blank=False, default="")


class Activity(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100, blank=False, default="")
