import django_filters
from .models import *

class MealFilter(django_filters.FilterSet):
    class Meta:
        model = Meal
        fields = ['Food_name','Category','Price','menu__Day']