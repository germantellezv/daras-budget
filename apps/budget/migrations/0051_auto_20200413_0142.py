# Generated by Django 3.0.4 on 2020-04-13 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0050_auto_20200413_0139'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='materialapu',
            name='performance',
        ),
        migrations.AddField(
            model_name='materialapu',
            name='unit',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
    ]