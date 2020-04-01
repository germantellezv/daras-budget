# Generated by Django 3.0.4 on 2020-04-01 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0024_auto_20200401_0049'),
    ]

    operations = [
        migrations.AddField(
            model_name='budgetitem',
            name='amount',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='budgetitem',
            name='total_value',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AddField(
            model_name='budgetitem',
            name='unit_value',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True),
        ),
    ]
