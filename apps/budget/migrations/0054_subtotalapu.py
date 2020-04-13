# Generated by Django 3.0.4 on 2020-04-13 17:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0053_budgetsubitem_budget'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubtotalAPU',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('workforce', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('material', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('equipment', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('transport', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('secure', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('total', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('budget', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='budget.Budget')),
                ('subitem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='budget.BudgetSubItem')),
            ],
            options={
                'verbose_name': 'General APU data',
            },
        ),
    ]
