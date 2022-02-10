from django import forms
from django.forms import ModelForm

from .models import *

class MealForm(ModelForm):
    class Meta:
        model = Meal
        fields = '__all__'

        



