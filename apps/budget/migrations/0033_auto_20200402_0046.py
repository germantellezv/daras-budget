# Generated by Django 3.0.4 on 2020-04-02 05:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0032_auto_20200402_0038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='unit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='budget.Unit'),
        ),
    ]