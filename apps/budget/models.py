from django.db import models

# Utilities
from django.utils.text import slugify
from django.utils.timezone import now

# Signals
from django.db.models.signals import post_save
from django.dispatch import receiver

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

class Unit(models.Model):
    """ Units for budget APU """
    acronym = models.CharField(unique=True, max_length=10)
    name = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return '{} - {}'.format(self.acronym, self.name)

    class Meta:
        verbose_name = 'unidad'
        verbose_name_plural = 'unidades'

class Material(models.Model):
    """ Materials model """

    name = models.CharField(max_length=100)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, blank=True, null=True, default=1)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, default=1)
    daily_price = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    slug = models.SlugField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        slug = '{0}-{1}'.format(self.name, now().strftime("%Y%m%d%H%M%S"))
        self.slug = slugify(slug)
        super(Material, self).save(*args, **kwargs)

    def __str__(self):
        return '{0} - {1}'.format(self.unit, self.name)

    class Meta:
        verbose_name = 'material'
        verbose_name_plural = 'materiales'

class Equipment(models.Model):
    """ Equipments and tools model """

    name = models.CharField(max_length=100)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, default=1)
    daily_price = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    slug = models.SlugField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        slug = '{0}-{1}'.format(self.name, now().strftime("%Y%m%d%H%M%S"))
        self.slug = slugify(slug)
        super(Equipment, self).save(*args, **kwargs)

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        verbose_name = 'equipo/herramienta'
        verbose_name_plural = 'equipos/herramientas'

class Transport(models.Model):
    """ Transport model """

    name = models.CharField(max_length=100)
    daily_price = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    slug = models.SlugField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        slug = '{0}-{1}'.format(self.name, now().strftime("%Y%m%d%H%M%S"))
        self.slug = slugify(slug)
        super(Transport, self).save(*args, **kwargs)

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        verbose_name = 'transporte'
        verbose_name_plural = 'transportes'

class Secure(models.Model):
    """ Secure and others model """

    name = models.CharField(max_length=100)
    daily_price = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    slug = models.SlugField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        slug = '{0}-{1}'.format(self.name, now().strftime("%Y%m%d%H%M%S"))
        self.slug = slugify(slug)
        super(Secure, self).save(*args, **kwargs)

    def __str__(self):
        pass

    class Meta:
        verbose_name = 'seguro/otro'
        verbose_name_plural = 'seguros/otros'

class Budget(models.Model):
    """ Budget model """

    OPTIONS_IVA = [
        # (None, 'Calcular IVA con respecto a'),
        ('1', 'Subtotal'),
        ('2', 'Utilidad')
    ]
    OPTIONS_PERIOD = [
        # (None, 'Periodo de tiempo'),
        ('1', 'Por hora'),
        ('2', 'Por día'),
        ('3', 'Mensual')
    ]
    consecutive = models.CharField(max_length=10, blank=True, null=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, blank=True, null=True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, blank=True, null=True)
    subject = models.CharField(max_length=300, blank=True, null=True)
    risk = models.ForeignKey(Risk, on_delete=models.CASCADE, blank=True, null=True)
    time = models.CharField(choices=OPTIONS_PERIOD, max_length=20, blank=True, null=True)
    total_direct_cost = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    
    administration_percentage = models.SmallIntegerField(verbose_name="Porcentaje de administración", blank=True, null=True)
    administration = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    
    incidentals_percentaje = models.SmallIntegerField(verbose_name="Porcentaje de imprevistos", blank=True, null=True)
    incidentals = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    
    utility_percentage = models.SmallIntegerField(verbose_name="Porcentaje de utilidad", blank=True, null=True)
    utility = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)

    iva_option = models.CharField(choices=OPTIONS_IVA, max_length=50, verbose_name="Calcular IVA sobre", blank=True, null=True)
    iva = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)

    comment = models.TextField(blank=True, null=True)
    
    total_indirect_cost = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    subtotal = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    total = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    
    created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(blank=True, null=True)

    def __str__(self):
        return '{} - {} - {}'.format(self.client, self.service, self.subject)

    class Meta:
        verbose_name = "presupuesto"
        verbose_name_plural = "presupuestos"

class BudgetSubItem(models.Model):
    """ Budget subitem model """
    
    description = models.CharField(max_length=200)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    amount = models.PositiveSmallIntegerField(blank=True, null=True)
    unit_value = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    total_value = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)
    
    def __str__(self):
        return '(subitem) - {}'.format(self.description)

    class Meta:
        verbose_name = 'subitem de presupuesto'
        verbose_name_plural = 'subitems de presupuesto'

class BudgetItem(models.Model):
    """ Budget section """

    budget = models.ForeignKey(Budget, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    duration = models.SmallIntegerField(verbose_name="Duración(días)")
    subitems = models.ManyToManyField(BudgetSubItem)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    slug = models.SlugField(blank=True, null=True)

    def __str__(self):
        return 'Actividad del presupuesto {}'.format(self.budget.subject)

    class Meta:
        verbose_name = 'item de presupuesto'
        verbose_name_plural = 'items de presupuesto'



# @receiver(post_save, sender=BudgetSubItem)
# def update_stock(sender, instance, **kwargs):
#     """ Add BudgetSubitem ID at the end of its slug """
#     if not instance.slug:
#         slug = '{0}{1}'.format(instance.item.slug, instance.id)
#         instance.slug = slugify(slug)
#         instance.save()
 
  
   