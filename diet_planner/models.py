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

    def calculate_calorie_needs(self):
        # Example calculation of calorie needs using the Harris-Benedict formula
        if self.activity_level == "Sedentary":
            activity_factor = 1.2
        elif self.activity_level == "Lightly active":
            activity_factor = 1.375
        elif self.activity_level == "Moderately active":
            activity_factor = 1.55
        else:
            activity_factor = 1.725

        BMR = 88.362 + (13.397 * self.weight) + (4.799 * self.height) - (5.677 * self.age)
        calorie_needs = BMR * activity_factor

        # Adjust calorie needs based on the user's goal
        if self.goal == "Weight loss":
            calorie_needs *= 0.8
        elif self.goal == "Weight gain":
            calorie_needs *= 1.2

        return calorie_needs
