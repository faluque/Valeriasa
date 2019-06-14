from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CuentaCorrienteForm, CustomUserCreationForm, CustomUserChangeForm
from .models import usuarios, ctacte

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = usuarios
    list_display = ['username', 'tipoUsr']

admin.site.register(usuarios, CustomUserAdmin)

class CtaCteAdmin(admin.ModelAdmin):
    form=CuentaCorrienteForm
    model=ctacte
    list_display = ['nro_inquilino','fecha', 'detalle' ]
admin.site.register(ctacte, CtaCteAdmin)