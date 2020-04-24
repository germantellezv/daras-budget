# Generated by Django 3.0.4 on 2020-04-17 06:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0058_budgetsubitem_duration'),
    ]

    operations = [
        migrations.AddField(
            model_name='budget',
            name='aiu_over',
            field=models.CharField(blank=True, choices=[('1', 'Presupuesto'), ('2', 'APU')], max_length=50, null=True, verbose_name='Aplicar AIU sobre'),
        ),
        migrations.AddField(
            model_name='budget',
            name='delivery_time',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Tiempo de entrega'),
        ),
        migrations.AddField(
            model_name='budget',
            name='rev_number',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Numero de revisión'),
        ),
        migrations.AlterField(
            model_name='budget',
            name='client',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='budget.Client', verbose_name='Cliente'),
        ),
        migrations.AlterField(
            model_name='budget',
            name='comment',
            field=models.TextField(blank=True, null=True, verbose_name='Anotaciones'),
        ),
        migrations.AlterField(
            model_name='budget',
            name='consecutive',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Consecutivo'),
        ),
        migrations.AlterField(
            model_name='budget',
            name='iva',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True, verbose_name='Total IVA'),
        ),
        migrations.AlterField(
            model_name='budget',
            name='risk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='budget.Risk', verbose_name='Riesgo de la empresa'),
        ),
        migrations.AlterField(
            model_name='budget',
            name='service',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='budget.Service', verbose_name='Especialidad'),
        ),
        migrations.AlterField(
            model_name='budget',
            name='subject',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='Objeto'),
        ),
        migrations.AlterField(
            model_name='budget',
            name='time',
            field=models.CharField(blank=True, choices=[('1', 'Por hora'), ('2', 'Por día'), ('3', 'Mensual')], max_length=20, null=True, verbose_name='Rango de tarifas'),
        ),
    ]