from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    age = models.PositiveIntegerField()
    weight = models.PositiveIntegerField()
    height = models.PositiveIntegerField()
    activity_level = models.CharField(max_length=50)
    dietary_restriction = models.CharField(max_length=50)
    goal = models.CharField(max_length=50)
    workout_goal = models.CharField(max_length=50)
