from django.urls import path
from .views import create_profile, update_profile, diet_plan


urlpatterns = [
    path('create_profile/', create_profile, name='create_profile'),
    path('update_profile/', update_profile, name='update_profile'),
    path('diet_planner/', diet_plan, name='diet_planner'),
]
