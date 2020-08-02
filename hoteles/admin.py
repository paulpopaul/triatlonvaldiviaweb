# coding=utf-8
from django.contrib import admin

# Register your models here.
from .models import Dato

class DatoAdmin(admin.ModelAdmin):

    fieldsets = (
        (None, {
            'fields': (('nombre', 'sub_titulo'), ('tipo', 'estrellas'), ('pagina_web', 'telefono'))
        }),
        (None, {
            'fields': (('comuna', 'direccion'),('imagen')),
        }),
    )
    list_filter = ['tipo', 'comuna']


admin.site.register(Dato, DatoAdmin)