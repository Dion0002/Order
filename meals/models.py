
from django.db import models

from django.db.models import DO_NOTHING
from users.models import CustomUser
# Create your models here.
class Menu(models.Model):

    Day = models.CharField(max_length=100, null=True, blank=True)

    preview = models.BooleanField(default=False)

    def __str__(self):
        return self.Day


class Meal(models.Model):
    CATEGORY = (
        ('Appetizer', 'Appetizer'),
        ('Entree', 'Entree'),
        ('Dessert ', 'Dessert '),
        ('Drinks ', 'Drinks '),

    )

    Food_name = models.CharField(max_length=128, blank=True, null=True)
    Category = models.CharField(max_length=100, null=True, blank=True, choices=CATEGORY)
    Descriptions = models.TextField(max_length=128, blank=True, null=True)
    Price = models.DecimalField(decimal_places=2, max_digits=20, default=0.00, blank=True, null=True)
    menu = models.ManyToManyField(Menu, related_name='weeklymenu', blank=True)

    def __str__(self):
        return self.Food_name

class Order(models.Model):
    customer = models.ForeignKey(CustomUser,default="",on_delete=DO_NOTHING )
    bill = models.DecimalField(max_digits=4 , decimal_places=2)
    date = models.DateTimeField(auto_now_add=True,blank=True)
    number = models.CharField(max_length=60)
    def __str__(self):
        return f"{self.customer} {self.bill}"


class Item(models.Model):
    order = models.ForeignKey(Order,on_delete=DO_NOTHING)
    name  = models.CharField(max_length=120)
    price = models.DecimalField(max_digits=4,decimal_places=2)
    order_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"{self.order.customer} {self.name} {self.price}"






