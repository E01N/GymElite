from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)
    weight = models.FloatField()
    goal = models.CharField(max_length=10, choices=[("GAIN", "Weight Gain"), ("LOSS", "Weight Loss")])
    calories = models.IntegerField()


class Meal(models.Model):
    name = models.CharField(max_length=100)
    calories = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)