# Generated by Django 3.0.4 on 2020-03-29 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='clients',
            options={'verbose_name': 'cliente', 'verbose_name_plural': 'clientes'},
        ),
        migrations.AddField(
            model_name='clients',
            name='country',
            field=models.CharField(default='Colombia', max_length=50),
        ),
        migrations.AddField(
            model_name='clients',
            name='state',
            field=models.CharField(default='Bolívar', max_length=50),
        ),
        migrations.AlterField(
            model_name='clients',
            name='city',
            field=models.CharField(default='Cartagena', max_length=50),
        ),
    ]
