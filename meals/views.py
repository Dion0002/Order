from django.shortcuts import render, redirect,HttpResponse
from .forms import *
from datetime import date
from django.views.decorators.csrf import csrf_exempt
import random
import json
from .filters import *


# Create your views here.


def randomOrderNumber(length):
    sample = '123456789'
    numberO = ''.join((random.choice(sample) for i in range(length)))
    return numberO


def add_meal(request):
    if request.user.is_superuser:
        form = MealForm
        if request.method == 'POST':
            form = MealForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/meals/all_meal')
        context = {'form': form}
        return render(request, 'meals/add_meal.html', context)


def all_meal(request):
    if request.user.is_superuser:
        all_meal = Meal.objects.all()
        myFilter = MealFilter(request.GET, queryset=all_meal)
        all_meal = myFilter.qs
        context = {'all_meal': all_meal, 'MealFilter': myFilter}
        return render(request, 'meals/all_meal.html', context)


def updateMeal(request, pk):
    if request.user.is_superuser:
        all_meal = Meal.objects.get(id=pk)
        form = MealForm(instance=all_meal)
        if request.method == 'POST':
            form = MealForm(request.POST, instance=all_meal)
            if form.is_valid():
                form.save()
                return redirect('/meals/all_meal')
        context = {'form': form}
        return render(request, 'meals/update_meal.html', context)


def deleteMeal(request, pk):
    if request.user.is_superuser:
        all_meal = Meal.objects.get(id=pk)
        if request.method == 'POST':
            all_meal.delete()
            return redirect('/meals/all_meal')

        context = {'meal': all_meal}
        return render(request, 'meals/delete_meal.html', context)


def weekmenu(request):
  
    if date.today().weekday() == 0:
        WeekMenu = Meal.objects.filter(menu__Day='Monday').values(
            'id', 'Food_name', 'Category', 'Descriptions', 'Price')
    elif date.today().weekday() == 1:
        WeekMenu = Meal.objects.filter(menu__Day='Tuesday').values(
            'id', 'Food_name', 'Category', 'Descriptions', 'Price')
    elif date.today().weekday() == 2:
        WeekMenu = Meal.objects.filter(menu__Day='Wednesday').values(
            'id', 'Food_name', 'Category', 'Descriptions', 'Price')
    elif date.today().weekday() == 3:
        WeekMenu = Meal.objects.filter(menu__Day='Thursday').values(
            'id', 'Food_name', 'Category', 'Descriptions', 'Price')
    elif date.today().weekday() == 4:
        WeekMenu = Meal.objects.filter(menu__Day='Friday').values(
            'id', 'Food_name', 'Category', 'Descriptions', 'Price')
    else:
        return redirect("/meals/preview")
    return render(request, 'meals/WeeklyMenu.html', {'week_meal': WeekMenu})



def preview(request):
 
        display_menu = Meal.objects.filter(menu__preview=True).values(
            'id', 'Food_name', 'Category', 'Descriptions', 'Price')
        return render(request, 'meals/PREVIEW.html', {'week_meal': display_menu})


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


@csrf_exempt
def order(request):
        if request.method == 'POST':
            if is_ajax(request=request):
                request.session['orders'] = request.POST.get('order')
                orders = json.loads(request.session['orders'])
                request.session['bill'] = request.POST.get('total')
                randomNum = randomOrderNumber(6)

                while Order.objects.filter(number=randomNum).count() > 0:
                    randomNum = randomOrderNumber(6)

                if request.user.is_authenticated:
                    order = Order(customer=request.user,
                                number=randomOrderNumber(6),
                                bill=float(request.session['bill']))
                    order.save()
                    request.session['orderNum'] = order.number
                    for article in orders:
                        item = Item(
                            order=order,
                            name=article[0],
                            price=float(article[1])
                        )
                        item.save()

        return render(request, 'meals/order.html')


def success(request):
        orderNum = request.session['orderNum']
        bill = request.session['bill']
        items = Item.objects.filter(order__number=orderNum)
        context = {'order': order, 'bill': bill, 'items': items}
        return render(request, 'meals/success.html', context)


def orderdeteils(request):
    if request.user.is_superuser:
        all_orders = Order.objects.all()

        context = {'orders': all_orders}
        return render(request, 'meals/History_order.html', context)


def userorderdetail(request, pk):
    if request.user.is_superuser:
        user_order = Item.objects.filter(order=pk)
        return render(request, 'meals/more_detail_order.html', {'user_order': user_order})



def previousorder(request):
        user = request.user

        previous_order_m = Item.objects.filter(order__customer=user, order_date__iso_week_day=1)
        
        previous_order_tu = Item.objects.filter(order__customer=user, order_date__iso_week_day=2)
        previous_order_we = Item.objects.filter(order__customer=user, order_date__iso_week_day=3)
        
        
        previous_order_th = Item.objects.filter(order__customer=user, order_date__iso_week_day=4)
        previous_order_f = Item.objects.filter(order__customer=user, order_date__iso_week_day=5)
        
        context={'previous_order_m':previous_order_m,'previous_order_tu':previous_order_tu,'previous_order_we':previous_order_we,
        'previous_order_th':previous_order_th,'previous_order_f':previous_order_f,}

        return render(request, 'meals/previous_order.html', context)



