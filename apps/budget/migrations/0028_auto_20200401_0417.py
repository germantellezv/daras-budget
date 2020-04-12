# Generated by Django 3.0.4 on 2020-04-01 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0027_auto_20200401_0249'),
    ]

    operations = [
        migrations.AddField(
            model_name='budgetitem',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='budget',
            name='iva_option',
            field=models.CharField(choices=[(None, 'Calcular IVA con respecto a'), ('1', 'Subtotal'), ('2', 'Utilidad')], max_length=50, verbose_name='Calcular IVA sobre'),
        ),
    ]