# Generated by Django 3.0.4 on 2020-03-30 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0009_auto_20200330_0207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='metalmechanicworkforce',
            name='experience_time',
            field=models.CharField(choices=[(None, 'Años de experiencia'), ('0-3', '0-3 años'), ('3', '3 años'), ('+3', '+3 años'), ('3-5', '3-5 años'), ('5', '5 años'), ('+5', '+5 años'), ('5-10', '5-10 años'), ('10', '10 años'), ('+10', '+10 años')], max_length=20, verbose_name='Años de experiencia'),
        ),
    ]
