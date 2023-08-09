from django.db import models


class Account(models.Model):
    account_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=30, blank=False, default="")
    first_name = models.CharField(max_length=30, blank=False, default="")
