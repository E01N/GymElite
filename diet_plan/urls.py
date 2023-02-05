from django.urls import path
from . import views


urlpatterns = [
    path('create_user/', views.create_user, name='create_user'),
    path('create_meal/<int:user_id>/', views.create_meal, name='create_meal'),
]
