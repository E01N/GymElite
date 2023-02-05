from django.shortcuts import render, redirect
from .models import User, Meal

def create_user(request):
    if request.method == "POST":
        name = request.POST["name"]
        weight = request.POST["weight"]
        goal = request.POST["goal"]
        calories = 0
        if goal == "GAIN":
            calories = weight * 35
        elif goal == "LOSS":
            calories = weight * 30
        user = User.objects.create(
            name=name, weight=weight, goal=goal, calories=calories
        )
        return redirect("create_meal", user_id=user.id)
    return render(request, "create_user.html")

def create_meal(request, user_id):
    user = User.objects.get(id=user_id)
    if request.method == "POST":
        name = request.POST["name"]
        calories = request.POST["calories"]
        Meal.objects.create(name=name, calories=calories, user=user)
        return redirect("create_meal", user_id=user.id)
    meals = Meal.objects.filter(user=user)
    return render(request, "create_meal.html", {"user": user, "meals": meals})
