from django.contrib import admin
from .models import Diet, Exercise, DietPlan, ExercisePlan, Meal

admin.site.register(Diet)
admin.site.register(Exercise)
admin.site.register(DietPlan)
admin.site.register(ExercisePlan)
admin.site.register(Meal)
