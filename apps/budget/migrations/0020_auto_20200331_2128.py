# Generated by Django 3.0.4 on 2020-04-01 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0019_auto_20200331_2125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='budget',
            name='total_direct_cost',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='budget',
            name='utility',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True),
        ),
    ]
