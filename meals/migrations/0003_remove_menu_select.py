# Generated by Django 4.0.1 on 2022-01-30 18:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0002_menu_select_alter_meal_menu'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='Select',
        ),
    ]
