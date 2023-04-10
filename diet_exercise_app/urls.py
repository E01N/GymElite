from django.urls import path
from . import views

app_name = 'diet_exercise_app'

urlpatterns = [
    path('create_diet_plan/', views.create_diet_plan, name='create_diet_plan'),
    path('view_diet_plan/', views.view_diet_plan, name='view_diet_plan'),
    path('create_exercise_plan/', views.create_exercise_plan, name='create_exercise_plan'),
    path('view_exercise_plan/', views.view_exercise_plan, name='view_exercise_plan'),
]
