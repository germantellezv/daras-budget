from django.contrib import admin

# Models
from .models import Profile

# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    class Meta:
        verbose_name = "Perfil"