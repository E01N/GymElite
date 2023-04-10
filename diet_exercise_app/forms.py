from django import forms
from .models import Diet, Exercise, DietPlan, ExercisePlan


class DietForm(forms.ModelForm):
    class Meta:
        model = Diet
        fields = ['goal']
        widgets = {
            'goal': forms.Select(attrs={'class': 'form-select'}),
        }
        labels = {
            'goal': 'Goal',
        }


class ExercisePlanForm(forms.ModelForm):
    class Meta:
        model = ExercisePlan
        fields = ['goal', 'duration']
        widgets = {
            'goal': forms.Select(choices=ExercisePlan.GOAL_CHOICES, attrs={'class': 'form-select'}),
            'duration': forms.Select(choices=ExercisePlan.DURATION_CHOICES, attrs={'class': 'form-select'}),
        }
        labels = {
            'goal': 'Goal',
            'duration': 'Duration',
        }

