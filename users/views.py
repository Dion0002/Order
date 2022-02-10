
from django.shortcuts import render, redirect
from .models import  CustomUser
from .forms import *
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView 
from .filters import UsersFilter

# Create your views here.

def my_view(request):
    if request.user.is_superuser:
        return redirect('user-info')
    if request.user:    
      return render(request, 'meals/previous_order.html')




def user_info(request):
 if request.user.is_superuser:
        user_info = CustomUser.objects.all()

        myFilter = UsersFilter(request.GET, queryset=user_info)
        user_info = myFilter.qs

        contex = {'user_info': user_info, 'myFilter': myFilter}

        return render(request, 'users/user_info.html', contex)


class SignUpView(CreateView):
  
        model = CustomUser
        form_class = CustomerUserCreationForm
        success_url = reverse_lazy('signup')
        template_name = 'registration/signup.html'


class UserLoginPageView(LoginView):
    template_name = 'registration/login.html'


class UserLogout(LogoutView):
    template_name = 'registration/login.html'


def updateUsers(request, pk):
 if request.user.is_superuser:
        all_users = CustomUser.objects.get(id=pk)
        form = CustomerUserUpdateForm(instance=all_users)
        if request.method == 'POST':
            form = CustomerUserUpdateForm(request.POST, instance=all_users)
            if form.is_valid():
                form.save()
                return redirect('/users/user_info')
        context = {'form': form}
        return render(request, 'users/update_users.html', context)


def deleteUsers(request, pk):
     if request.user.is_superuser:
        all_users = CustomUser.objects.get(id=pk)
        if request.method == 'POST':
            all_users.delete()
            return redirect('/users/user_info')

        context = {'users': all_users}
        return render(request, 'users/delete_users.html', context)

        

class MyPasswordChangeView(PasswordChangeView):
    template_name = 'registration/password_change.html'
    success_url = reverse_lazy('password_change')
    

   

    
    

    
