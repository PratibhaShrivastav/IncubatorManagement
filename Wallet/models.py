from django.db import models
from django.contrib.auth.models import User


class Wallet(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='wallet')
    coffee_total = models.IntegerField(default=0)
    rent_total = models.IntegerField(default=0)
    balance = models.IntegerField(default=1000)

    def __str__(self):
        return self.user.username + '-Wallet'