# Generated by Django 4.0.1 on 2022-02-02 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0006_alter_item_name_alter_menu_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(max_length=120),
        ),
    ]
