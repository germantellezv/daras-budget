# Generated by Django 3.0.4 on 2020-05-23 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0005_auto_20200523_0100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
