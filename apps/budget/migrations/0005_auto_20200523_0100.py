# Generated by Django 3.0.4 on 2020-05-23 06:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0004_auto_20200520_1915'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='category',
            field=models.ForeignKey(default=21, on_delete=django.db.models.deletion.CASCADE, to='budget.ActivityCategory'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='service',
            field=models.ForeignKey(default=6, on_delete=django.db.models.deletion.CASCADE, to='budget.Service'),
        ),
        migrations.AlterField(
            model_name='client',
            name='created',
            field=models.DateTimeField(),
        ),
    ]
