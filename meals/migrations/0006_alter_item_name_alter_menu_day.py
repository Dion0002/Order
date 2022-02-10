# Generated by Django 4.0.1 on 2022-02-02 16:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0005_rename_user_order_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='meals.meal'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='Day',
            field=models.CharField(blank=True, choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday')], max_length=100, null=True),
        ),
    ]
