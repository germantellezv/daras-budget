from django.db import models

# Utilities
from django.utils.text import slugify
from django.utils.timezone import now


# Create your models here.

class Client(models.Model):
    """ Client Model """
    nit = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=50, default="Colombia")
    state = models.CharField(max_length=50, default="Bolívar")
    city = models.CharField(max_length=50, default="Cartagena")
    address = models.CharField(max_length=100, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "cliente"
        verbose_name_plural = "clientes"

    def __str__(self):
        return '{} - {}'.format(self.nit, self.name)


class Service(models.Model):
    """ Type of service Model """
    name = models.CharField(max_length=100)
    photo = models.ImageField(blank=True, null=True)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Service, self).save(*args, **kwargs)

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        verbose_name = "tipo de servicio"
        verbose_name_plural = "tipos de servicio"


class Workforce(models.Model):
    """ Workforce model """
    EXPERIENCE_YEARS = [
        (None, 'Años de experiencia'),
        ('0-3', '0-3 años'),
        ('3', '3 años'),
        ('+3', '+3 años'),
        ('3-5', '3-5 años'),
        ('5', '5 años'),
        ('+5', '+5 años'),
        ('5-10', '5-10 años'),
        ('10', '10 años'),
        ('+10', '+10 años'),
    ]
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name="Nombre")
    experience_time = models.CharField(
        choices=EXPERIENCE_YEARS, max_length=20, blank=True, null=True, verbose_name="Años de experiencia")
    daily_salary = models.DecimalField(max_digits=15, decimal_places=2, verbose_name="Salario por día",
                                       help_text="ATENCIÓN: Esta cifra siempre debe terminar con dos decimales y no se colocan punto de mil o millón.")
    created = models.DateTimeField(
        auto_now_add=True, verbose_name="Fecha de creación")
    modified = models.DateTimeField(
        auto_now=True, verbose_name="Última modificación")

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        verbose_name = "mano de obra"
        verbose_name_plural = "manos de obra"


class Risk(models.Model):
    """ Risk type model """
    name = models.CharField(max_length=20, verbose_name="Nombre")
    value = models.DecimalField(
        max_digits=3, decimal_places=2, verbose_name="Valor")

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        verbose_name = "tipo de riesgo"
        verbose_name_plural = "tipos de riesgo"


class Budget(models.Model):
    """ Budget model """

    OPTIONS_IVA = [
        (None, 'Calcular IVA con respecto a'),
        ('1', 'Subtotal'),
        ('2', 'XXXXXXXX')
    ]
    OPTIONS_PERIOD = [
        (None, 'Periodo de tiempo'),
        ('1', 'Por hora'),
        ('2', 'Por día'),
        ('3', 'Mensual')
    ]

    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    subject = models.CharField(max_length=300, blank=True, null=True)
    risk = models.ForeignKey(Risk, on_delete=models.CASCADE)
    time = models.CharField(choices=OPTIONS_PERIOD, max_length=20)
    total_direct_cost = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    
    administration_percentage = models.SmallIntegerField(verbose_name="Porcentaje de administración")
    administration = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    
    incidentals_percentaje = models.SmallIntegerField(verbose_name="Porcentaje de imprevistos")
    incidentals = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    
    utility_percentage = models.SmallIntegerField(verbose_name="Porcentaje de utilidad")
    utility = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)

    iva_option = models.CharField(choices=OPTIONS_IVA, max_length=50, verbose_name="Calcular IVA sobre")
    iva = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)

    comment = models.TextField(blank=True, null=True)
    
    total_indirect_cost = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    subtotal = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    total = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    
    created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(blank=True, null=True)

    def __str__(self):
        return '{} - {} - {}'.format(self.client, self.service, self.subject)

    def save(self, *args, **kwargs):
        slug = '{0}{1}'.format(self.client.nit, now().strftime("%Y%m%d%H%M%S"))
        self.slug = slugify(slug)
        super(Budget, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "presupuesto"
        verbose_name_plural = "presupuestos"
