from django.shortcuts import render, redirect
from .models import UserProfile
from .forms import UserProfileForm
from django.contrib.auth.decorators import login_required


def create_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            user_profile = form.save()
            return redirect('diet_plan', pk=user_profile.pk)
    else:
        form = UserProfileForm()
    return render(request, 'create_profile.html', {'form': form})

def update_profile(request, pk):
    user_profile = UserProfile.objects.get(pk=pk)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            user_profile = form.save()
            return redirect('diet_plan', pk=user_profile.pk)
    else:
        form = UserProfileForm(instance=user_profile)
    return render(request, 'update_profile.html', {'form': form})

@login_required
def diet_plan(request):
    age = int(request.POST.get('age'))
    weight = int(request.POST.get('weight'))
    height = int(request.POST.get('height'))
    activity_level = request.POST.get('activity_level')
    goal = request.POST.get('goal')
    calorie_needs = calculate_calorie_needs(age, weight, height, activity_level, goal)
    foods = generate_diet_plan(calorie_needs)
    return render(request, 'diet_plan.html', {
        'calorie_needs': calorie_needs,
        'foods': foods
    })

def calculate_calorie_needs(age, weight, height, gender, activity_level, goal):
    weight_in_kg = weight / 2.2
    height_in_cm = height * 2.54
    if gender == 'male':
        BMR = 88.362 + (13.397 * weight_in_kg) + (4.799 * height_in_cm) - (5.677 * age)
    else:
        BMR = 447.593 + (9.247 * weight_in_kg) + (3.098 * height_in_cm) - (4.330 * age)
    if activity_level == 'sedentary':
        TDEE = BMR * 1.2
    elif activity_level == 'lightly_active':
        TDEE = BMR * 1.375
    elif activity_level == 'moderately_active':
        TDEE = BMR * 1.55
    elif activity_level == 'very_active':
        TDEE = BMR * 1.725
    else:
        TDEE = BMR * 1.9
    if goal == 'weight_loss':
        calorie_needs = TDEE - 500
    elif goal == 'maintenance':
        calorie_needs = TDEE
    else:
        calorie_needs = TDEE + 500
    return calorie_needs


def generate_diet_plan(user_profile):
    # Example implementation: return a list of foods that meet the user's dietary restrictions and calorie needs
    foods = [
        {"name": "Eggs", "calories": 155, "protein": 12, "fat": 11, "carbohydrates": 1},
        {"name": "Oatmeal", "calories": 150, "protein": 5, "fat": 3, "carbohydrates": 27},
        {"name": "Almonds", "calories": 162, "protein": 6, "fat": 14, "carbohydrates": 6},
        {"name": "Chicken breast", "calories": 165, "protein": 31, "fat": 3, "carbohydrates": 0},
        {"name": "Brown rice", "calories": 216, "protein": 5, "fat": 2, "carbohydrates": 45},
    ]

    # Filter foods based on the user's dietary restrictions
    if user_profile.dietary_restriction == "Vegetarian":
        foods = [food for food in foods if food["name"] not in ["Chicken breast"]]
    elif user_profile.dietary_restriction == "Vegan":
        foods = [food for food in foods if food["name"] not in ["Eggs", "Chicken breast"]]

    return foods

def generate_workout_plan(user_profile):
    # Example implementation: return a list of exercises based on the user's workout goal
    if user_profile.workout_goal == "Muscle gain":
        exercises = ["Barbell squat", "Deadlift", "Barbell bench press", "Dumbbell rows"]
    elif user_profile.workout_goal == "Fat loss":
        exercises = ["Running", "Cycling", "Swimming", "Jump rope"]
    else:
        exercises = ["Barbell squat", "Deadlift", "Barbell bench press", "Dumbbell rows", "Running", "Cycling", "Swimming", "Jump rope"]

    return exercises

