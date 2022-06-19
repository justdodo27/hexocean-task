from django.db import models
from django.contrib.auth.models import AbstractUser
from tiersapp.models import Tier

# Create your models here.
class CustomUser(AbstractUser):
    tier = models.ForeignKey(Tier, on_delete=models.CASCADE, null=True, default=None)