# Generated by Django 3.0.4 on 2020-04-03 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0041_auto_20200402_2158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='budgetsubitem',
            name='total_value',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True),
        ),
    ]