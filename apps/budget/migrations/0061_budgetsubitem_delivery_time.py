# Generated by Django 3.0.4 on 2020-04-18 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0060_auto_20200418_0040'),
    ]

    operations = [
        migrations.AddField(
            model_name='budgetsubitem',
            name='delivery_time',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Tiempo de entrega'),
        ),
    ]