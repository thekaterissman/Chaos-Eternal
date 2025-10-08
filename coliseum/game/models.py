from django.db import models
from django.contrib.auth.models import User

class PlayerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    level = models.IntegerField(default=1)
    character_name = models.CharField(max_length=50, default='Kate')

    def __str__(self):
        return f"{self.user.username}'s Profile"
