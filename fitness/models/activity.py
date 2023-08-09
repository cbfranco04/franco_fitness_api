from django.db import models
from .account import Account


class Activity(models.Model):
    activity_id = models.AutoField(primary_key=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='activities')
    title = models.CharField(max_length=100, blank=False, default="")
