from django.urls import path

from .views import *
from users.views import *

app_name='meal'

urlpatterns = [



    path('all_meal/', all_meal, name='all-meal'),
    path('add_meal/', add_meal, name='add-meal'),
    path('update_meal/<int:pk>', updateMeal, name='update-meal'),
    path('delete_meal/<int:pk>', deleteMeal, name='delete-meal'),

    path('week_meal/', weekmenu, name='week-meal'),
    path('preview/', preview, name='preview'),
    path('order/', order, name='order'),
    path('History_order/', orderdeteils, name='order-details'),
    path('user_order/<int:pk>', userorderdetail, name='user-order'),

    path('previous_order_user/', previousorder, name='previous-order-user'),

    path('success/', success, name='success'),




]
