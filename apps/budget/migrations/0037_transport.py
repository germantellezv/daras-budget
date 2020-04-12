# Generated by Django 3.0.4 on 2020-04-02 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0036_equipment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('daily_price', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('slug', models.SlugField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'transporte',
                'verbose_name_plural': 'transportes',
            },
        ),
    ]