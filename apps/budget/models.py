from django.db import models

# Utilities
from django.utils.text import slugify


# Create your models here.

class Clients(models.Model):
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

class Services(models.Model):
    """ Type of service Model """
    name = models.CharField(max_length=100)
    photo = models.ImageField(blank=True, null=True)
    slug = models.SlugField()
    class Meta:
        verbose_name = "tipo de servicio"
        verbose_name_plural = "tipos de servicio"
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Services, self).save(*args, **kwargs)

    def __str__(self):
        return '{}'.format(self.name)

class Budget(models.Model):
    """ Budget Model """

    OPTIONS_IVA = [
        (None,'Calcular iva con respecto a'),
        (1,'SUBTOTAL'),
        (2,'XXXXXXXX')
    ]
    client = models.ForeignKey(Clients, on_delete=models.CASCADE)
    service = models.ForeignKey(Services, on_delete=models.CASCADE)
    subject = models.CharField(max_length=300, blank=True, null=True)
    total_direct_cost = models.DecimalField(max_digits=15,decimal_places=2)
    administration_percentage = models.SmallIntegerField(verbose_name="Porcentaje de administración")
    administration = models.DecimalField(max_digits=15,decimal_places=2)
    incidentals_percentaje = models.SmallIntegerField(verbose_name="Porcentaje de imprevistos")
    incidentals = models.DecimalField(max_digits=15,decimal_places=2)
    utility_percentage = models.SmallIntegerField(verbose_name="Porcentaje de utilidad")
    utility = models.DecimalField(max_digits=15,decimal_places=2)
    total_indirect_cost = models.DecimalField(max_digits=15,decimal_places=2)
    subtotal = models.DecimalField(max_digits=15,decimal_places=2)
    iva_option = models.CharField(choices=OPTIONS_IVA, max_length=50, verbose_name="Calcular IVA sobre")
    iva = models.DecimalField(max_digits=15,decimal_places=2)
    total = models.DecimalField(max_digits=15,decimal_places=2)
    comment = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(blank=True, null=True)

    class Meta:
        verbose_name = "presupuesto"
        verbose_name_plural = "presupuestos"

    def __str__(self):
        return '{}-{}-{}'.format(self.client,self.service, self.subject)
    
    def save(self, *args, **kwargs):
        slug = '{0}{1}'.format(self.client.nit, self.created)
        self.slug = slugify(slug)
        super(Budget, self).save(*args, **kwargs)