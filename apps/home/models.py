from django.db import models

# Models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    """ Profile Model """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_client = models.BooleanField(default=True)
    image = models.ImageField(blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    phone = models.CharField(max_length=10 ,blank=True, null=True)
    
    def __str__(self):
        return '{}'.format(self.user.username)
    
    class Meta:
        verbose_name = 'perfil de usuario'
        verbose_name_plural = 'perfiles de usuario'
    