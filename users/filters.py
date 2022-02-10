import django_filters
from .models import *

class UsersFilter(django_filters.FilterSet):
    class Meta:
        model = CustomUser
        fields = ['username','user_role', 'Departament']