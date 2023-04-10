from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import DietPlanForm, ExercisePlanForm
from .models import Diet, Exercise, DietPlan, ExercisePlan

@login_required
def create_diet_plan(request):
    if request.method == 'POST':
        form = DietPlanForm(request.POST)
        if form.is_valid():
            diet_plan = form.save(commit=False)
            diet_plan.user = request.user
            diet_plan.save()
            return redirect('diet_exercise_app:view_diet_plan')
    else:
        form = DietPlanForm()
    return render(request, 'diet_exercise_app/create_diet_plan.html', {'form': form})

@login_required
def create_exercise_plan(request):
    if request.method == 'POST':
        form = ExercisePlanForm(request.POST)
        if form.is_valid():
            exercise_plan = form.save(commit=False)
            exercise_plan.user = request.user
            exercise_plan.save()
            return redirect('diet_exercise_app:view_exercise_plan')
    else:
        form = ExercisePlanForm()
    return render(request, 'diet_exercise_app/create_exercise_plan.html', {'form': form})

@login_required
def view_diet_plan(request):
    diet_plans = DietPlan.objects.filter(user=request.user)
    return render(request, 'diet_exercise_app/view_diet_plan.html', {'diet_plans': diet_plans})

@login_required
def view_exercise_plan(request):
    exercise_plans = ExercisePlan.objects.filter(user=request.user)
    return render(request, 'diet_exercise_app/view_exercise_plan.html', {'exercise_plans': exercise_plans})
