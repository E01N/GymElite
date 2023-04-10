from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import DietForm, ExercisePlanForm
from .models import Diet, Exercise, DietPlan, ExercisePlan, Meal
from datetime import datetime, timedelta


sample_meals = [
    {'name': 'Scrambled Eggs', 'description': 'Scrambled eggs with vegetables', 'calories': 300},
    {'name': 'Oatmeal', 'description': 'Oatmeal with fruits and nuts', 'calories': 450},
    {'name': 'Turkey Sandwich', 'description': 'Turkey sandwich with whole-grain bread and vegetables', 'calories': 500},
    {'name': 'Grilled Chicken Salad', 'description': 'Grilled chicken salad with mixed greens and vinaigrette', 'calories': 450},
    {'name': 'Salmon', 'description': 'Grilled salmon with quinoa and steamed vegetables', 'calories': 700},
    {'name': 'Pasta', 'description': 'Whole-grain pasta with tomato sauce and vegetables', 'calories': 650},
    {'name': 'Greek Yogurt', 'description': 'Greek yogurt with honey and berries', 'calories': 200},
    {'name': 'Almonds', 'description': 'A handful of almonds', 'calories': 160},
]


def create_sample_meals():
    for meal_data in sample_meals:
        meal, created = Meal.objects.get_or_create(name=meal_data['name'], defaults=meal_data)


def create_diet_plan(request):
    create_sample_meals()
    if request.method == 'POST':
        form = DietForm(request.POST)
        if form.is_valid():
            diet = form.save(commit=False)
            diet.user = request.user
            diet.save()

            current_date = datetime.now().date()
            end_date = current_date + timedelta(days=30)

            diet_plan = DietPlan(user=request.user, diet=diet)
            diet_plan.start_date = current_date
            diet_plan.end_date = end_date
            diet_plan.save()

            # Create sample meals if they don't exist
            create_sample_meals()

            # Generate meals based on user's diet.goal
            breakfast_meals, lunch_meals, dinner_meals, snack_meals = generate_meals(diet.goal)

            # Add meals to the diet plan
            diet_plan.breakfast.set(breakfast_meals)
            diet_plan.lunch.set(lunch_meals)
            diet_plan.dinner.set(dinner_meals)
            diet_plan.snack.set(snack_meals)
            diet_plan.save()

            return redirect('diet_exercise_app:view_diet_plan')
    else:
        form = DietForm()
    return render(request, 'diet_exercise_app/create_diet_plan.html', {'form': form})


def generate_meals(goal):
    # Create sample meals if they don't exist
    create_sample_meals()

    if goal == 'weight_loss':
        breakfast_meals = Meal.objects.filter(calories__lt=400)
        lunch_meals = Meal.objects.filter(calories__lt=500)
        dinner_meals = Meal.objects.filter(calories__lt=600)
        snack_meals = Meal.objects.filter(calories__lt=200)
    elif goal == 'weight_gain':
        breakfast_meals = Meal.objects.filter(calories__gt=600)
        lunch_meals = Meal.objects.filter(calories__gt=700)
        dinner_meals = Meal.objects.filter(calories__gt=800)
        snack_meals = Meal.objects.filter(calories__gt=300)
    else:  # Maintain
        breakfast_meals = Meal.objects.filter(calories__range=(400, 600))
        lunch_meals = Meal.objects.filter(calories__range=(500, 700))
        dinner_meals = Meal.objects.filter(calories__range=(600, 800))
        snack_meals = Meal.objects.filter(calories__range=(200, 300))

    return breakfast_meals, lunch_meals, dinner_meals, snack_meals


def create_exercise_plan(request):
    if request.method == 'POST':
        goal = request.POST['goal']
        duration = request.POST['duration']
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']
        day_1 = request.POST.getlist('day_1')
        day_2 = request.POST.getlist('day_2')
        day_3 = request.POST.getlist('day_3')

        exercise_plan = ExercisePlan(user=request.user, goal=goal, duration=duration,
                                      start_date=start_date, end_date=end_date)
        exercise_plan.save()
        exercise_plan.exercise_day_1.add(*day_1)
        exercise_plan.exercise_day_2.add(*day_2)
        exercise_plan.exercise_day_3.add(*day_3)
        
        return redirect('diet_exercise_app:view_exercise_plan')

    exercises = Exercise.objects.all()
    context = {'exercises': exercises}
    return render(request, 'diet_exercise_app/create_exercise_plan.html', context)


def view_diet_plan(request):
    diet_plans = DietPlan.objects.filter(user=request.user).order_by('-start_date')
    return render(request, 'diet_exercise_app/view_diet_plan.html', {'diet_plans': diet_plans})


def view_exercise_plan(request):
    latest_exercise_plan = ExercisePlan.objects.filter(user=request.user).order_by('-start_date').first()
    context = {'latest_exercise_plan': latest_exercise_plan}
    return render(request, 'diet_exercise_app/view_exercise_plan.html', context)
