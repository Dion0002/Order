from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import DO_NOTHING


# Create your models here.

class UserRole(models.Model):
    name = models.CharField(max_length=128, blank=True, null=True)

    def __str__(self):
        return self.name


class Departament(models.Model):
    Departament = models.CharField(max_length=128, blank=True, null=True)

    def __str__(self):
        return self.Departament


class CustomUser(AbstractUser):
    money =models.DecimalField(decimal_places=2, max_digits=20, default=5, blank=True, null=True)
    user_role = models.ForeignKey(UserRole, on_delete=DO_NOTHING, blank=True, null=True)
    Departament = models.ForeignKey(Departament, on_delete=DO_NOTHING, blank=True, null=True)










