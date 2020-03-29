# Generated by Django 3.0.4 on 2020-03-29 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0003_budget_services'),
    ]

    operations = [
        migrations.AlterField(
            model_name='budget',
            name='administration_percentage',
            field=models.SmallIntegerField(verbose_name='Porcentaje de administración'),
        ),
        migrations.AlterField(
            model_name='budget',
            name='incidentals_percentaje',
            field=models.SmallIntegerField(verbose_name='Porcentaje de imprevistos'),
        ),
        migrations.AlterField(
            model_name='budget',
            name='utility_percentage',
            field=models.SmallIntegerField(verbose_name='Porcentaje de utilidad'),
        ),
    ]
