# Generated by Django 3.0.4 on 2020-03-30 08:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0012_auto_20200330_0324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='budget',
            name='period',
            field=models.CharField(choices=[(None, 'Periodo de tiempo'), (1, 'Por hora'), (2, 'Por día'), (3, 'Mensual')], max_length=20),
        ),
        migrations.AlterField(
            model_name='budget',
            name='risk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='budget.Risk'),
        ),
    ]
