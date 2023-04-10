from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Diet(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    GOALS = (
        ('weight_loss', 'Weight Loss'),
        ('weight_gain', 'Weight Gain'),
        ('maintain', 'Maintain'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    age = models.IntegerField(null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True)
    height_cm = models.IntegerField(null=True)
    weight_lbs = models.FloatField(null=True)
    goal = models.CharField(max_length=50, choices=GOALS, default='maintain', null=True)

    def __str__(self):
        return f"{self.user.username}'s Diet Plan"


class Exercise(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.IntegerField() # in minutes


class DietPlan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    diet = models.ForeignKey(Diet, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()


class ExercisePlan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    frequency = models.IntegerField() # number of times per week
