# Generated by Django 3.0.4 on 2020-04-02 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0031_auto_20200402_0036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='daily_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True),
        ),
    ]