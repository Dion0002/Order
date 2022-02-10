# Generated by Django 4.0.1 on 2022-02-03 14:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Day', models.CharField(blank=True, max_length=100, null=True)),
                ('preview', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bill', models.DecimalField(decimal_places=2, max_digits=4)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('number', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Food_name', models.CharField(blank=True, max_length=128, null=True)),
                ('Category', models.CharField(blank=True, choices=[('Appetizer', 'Appetizer'), ('Entree', 'Entree'), ('Dessert ', 'Dessert '), ('Drinks ', 'Drinks ')], max_length=100, null=True)),
                ('Descriptions', models.TextField(blank=True, max_length=128, null=True)),
                ('Price', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True)),
                ('menu', models.ManyToManyField(blank=True, related_name='weeklymenu', to='meals.Menu')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('price', models.DecimalField(decimal_places=2, max_digits=4)),
                ('order_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='meals.order')),
            ],
        ),
    ]
