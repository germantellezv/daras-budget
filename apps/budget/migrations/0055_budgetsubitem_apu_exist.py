# Generated by Django 3.0.4 on 2020-04-13 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0054_subtotalapu'),
    ]

    operations = [
        migrations.AddField(
            model_name='budgetsubitem',
            name='apu_exist',
            field=models.BooleanField(default=False),
        ),
    ]
