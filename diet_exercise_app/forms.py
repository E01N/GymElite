from django import forms
from .models import Diet, Exercise, DietPlan, ExercisePlan


class DietPlanForm(forms.ModelForm):
    class Meta:
        model = Diet
        fields = ['age', 'gender', 'height_cm', 'weight_lbs', 'goal']


class ExercisePlanForm(forms.ModelForm):
    class Meta:
        model = ExercisePlan
        fields = ['exercise', 'start_date', 'end_date', 'frequency']

