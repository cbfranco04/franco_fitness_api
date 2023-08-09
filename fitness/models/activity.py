from django.db import models
from .account import Account


class Activity(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE, null=True, related_name='activities')
    title = models.CharField(max_length=100, blank=False, default="")
