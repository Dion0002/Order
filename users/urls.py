from re import template
from unicodedata import name
from django.urls import path , re_path


from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Login page path
    path('', UserLoginPageView.as_view(), name='login'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('logout/', UserLogout.as_view(), name='logout'),

    # Home page path
    re_path(r'my_view', my_view, name='my_view'),
 
   


    # User Info
    path('user_info/', user_info, name='user-info'),
    path('update_users/<int:pk>', updateUsers, name='update-users'),
    path('delete_users/<int:pk>', deleteUsers, name='delete-users'),

    #User Page
    
    # path('previous_order_user/', my_view, name='previous-order-user'),

    #reset password
     path('change_password/', MyPasswordChangeView.as_view(),name='password_change'),




]
