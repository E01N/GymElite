from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


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


class Meal(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    calories = models.IntegerField()

    def __str__(self):
        return self.name


class DietPlan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    diet = models.ForeignKey(Diet, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    breakfast = models.ManyToManyField(Meal, related_name='breakfast_meals')
    lunch = models.ManyToManyField(Meal, related_name='lunch_meals')
    dinner = models.ManyToManyField(Meal, related_name='dinner_meals')
    snack = models.ManyToManyField(Meal, related_name='snack_meals')


class Exercise(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.IntegerField() # in minutes
    muscle_group = models.CharField(max_length=100)


class ExercisePlan(models.Model):
    GOAL_CHOICES = [
        ('weight_loss', 'Weight Loss'),
        ('weight_gain', 'Weight Gain'),
        ('maintain', 'Maintain'),
    ]

    DURATION_CHOICES = (
        (7, '1 week'),
        (14, '2 weeks'),
        (30, '1 month'),
        (90, '3 months'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    goal = models.CharField(max_length=20, choices=GOAL_CHOICES)
    duration = models.CharField(max_length=20, choices=DURATION_CHOICES)
    start_date = models.DateField()
    end_date = models.DateField()
    exercise_day_1 = models.ManyToManyField(Exercise, related_name='day_1')
    exercise_day_2 = models.ManyToManyField(Exercise, related_name='day_2')
    exercise_day_3 = models.ManyToManyField(Exercise, related_name='day_3')

    def __str__(self):
        return f"{self.user.username}'s {self.goal} Plan for {self.duration} Weeks"


# create instances of the Exercise model with the new exercises
Exercise.objects.create(name='Bench Press', muscle_group='Chest', description='Lie on a bench and lift a barbell to chest level')
Exercise.objects.create(name='Squat', muscle_group='Legs', description='Stand with a barbell on your back and squat down')
Exercise.objects.create(name='Deadlift', muscle_group='Back', description='Lift a barbell off the ground with your legs and back')

# add the new exercises to the ExercisePlan model's exercise_day_1, exercise_day_2, and exercise_day_3 fields
exercise_day_1 = Exercise.objects.filter(name__in=['Bench Press', 'Squat'])
exercise_day_2 = Exercise.objects.filter(name__in=['Deadlift', 'Squat'])
exercise_day_3 = Exercise.objects.filter(name__in=['Bench Press', 'Deadlift'])
user = User.objects.first() # get the first user object from the database
exercise_plan = ExercisePlan.objects.create(user=user, goal='weight_loss', duration='7', start_date=timezone.now(), end_date=timezone.now())
exercise_plan.exercise_day_1.add(*exercise_day_1)
exercise_plan.exercise_day_2.add(*exercise_day_2)
exercise_plan.exercise_day_3.add(*exercise_day_3)


class ExercisePlan(models.Model):
    GOAL_CHOICES = [
        ('weight_loss', 'Weight Loss'),
        ('weight_gain', 'Weight Gain'),
        ('maintain', 'Maintain'),
    ]

    DURATION_CHOICES = (
        (7, '1 week'),
        (14, '2 weeks'),
        (30, '1 month'),
        (90, '3 months'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    goal = models.CharField(max_length=20, choices=GOAL_CHOICES)
    duration = models.CharField(max_length=20, choices=DURATION_CHOICES)
    start_date = models.DateField()
    end_date = models.DateField()
    exercise_day_1 = models.ManyToManyField(Exercise, related_name='day_1')
    exercise_day_2 = models.ManyToManyField(Exercise, related_name='day_2')
    exercise_day_3 = models.ManyToManyField(Exercise, related_name='day_3')

    def __str__(self):
        return f"{self.user.username}'s {self.goal} Plan for {self.duration} Weeks"