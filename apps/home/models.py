from django.db import models

# Models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    """ Profile Model """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=255 ,blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    class Meta:
        verbose_name = 'perfil de usuario'
        verbose_name_plural = 'perfiles de usuario'
    
    def __str__(self):
        return '{}'.format(self.user.username)