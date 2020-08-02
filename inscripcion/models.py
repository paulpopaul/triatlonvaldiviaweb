# coding=utf-8
from __future__ import unicode_literals

import datetime
from time import timezone

from django.db import models

# Create your models here.

#
CHOICES_SEXO = (
    ('HOMBRE', 'Hombre'),
    ('MUJER', 'Mujer'),
)
CHOICES_DISTANCIA = (
    ('Media', 'Media'),
    ('Entera', 'Entera'),
)
CHOICES_TALLA = (
    ('XS', 'XS'),
    ('S', 'S'),
    ('M', 'M'),
    ('L', 'L'),
    ('XL', 'XL'),
)
CHOICES_EDAD_PRECIO = (
    ('ELITE', 'Elite'),
    ('INFANTILES', 'Infantiles'),
    ('JUVENILES', 'Juveniles'),
    ('ADULTOS', 'Adultos'),
)

CHOICES_PAGO = (
    # ('WEBPAY', 'WebPay'),
    ('TRANSF', 'Transferencia'),
)

from django.utils.deconstruct import deconstructible


class CategoriaACompetir(models.Model):
    nombre_categoria = models.CharField(choices=CHOICES_EDAD_PRECIO, max_length=15)
    distancia = models.CharField(choices=CHOICES_DISTANCIA, max_length=15, blank=True, null=True)
    edad = models.CharField(max_length=8)
    precio = models.CharField(max_length=12)

    def __unicode__(self):
        return u"%s (Distancia: %s / Precio: %sCLP)" % (self.nombre_categoria, self.distancia, self.precio)

    class Meta:
        verbose_name_plural = 'Categorías a Competir'
        verbose_name = 'Categoría a Competir'


class Persona(models.Model):
    anno = models.PositiveSmallIntegerField(default=2017, null=True, blank=True)
    pagado = models.BooleanField(default=False, help_text='Marcar si se realizó la transferencia')
    rut = models.CharField('RUT', max_length=15,
                           help_text='12345678-5',
                           unique=True
                           )
    nombre = models.CharField('Nombre', max_length=16, help_text='Alvaro')
    apellido_pat = models.CharField('Apellido Paterno', max_length=16, help_text='Alvarado')
    apellido_mat = models.CharField('Apellido Materno', max_length=16, help_text='Aguirre')
    sexo = models.CharField(max_length=6, choices=CHOICES_SEXO, default='HOMBRE')
    email = models.EmailField()
    fecha_nacimiento = models.DateField('Fecha de Nacimiento')

    telefono = models.CharField('Teléfono', max_length=16)
    celular = models.CharField('Celular', max_length=16)
    comuna = models.CharField(max_length=16, help_text='En caso de ser Chilen', null=True, blank=True, )
    nacionalidad = models.CharField(max_length=16)
    direccion = models.CharField('Dirección', max_length=64)
    club = models.CharField('Club', max_length=32, null=True, blank=True)
    talla_polera = models.CharField('Talla de Polera', default='M', max_length=2, choices=CHOICES_TALLA, null=False, blank=False)
    medio_pago = models.CharField('Medio de Pago', max_length=8, choices=CHOICES_PAGO, default='TRANSFERENCIA')
    edad_y_precio = models.ForeignKey(
        CategoriaACompetir,
        related_name='categoria_persona',
        # null=True, blank=True,

    )

    def estado(self):
        if (self.pagado == 1):
            return 'Si'
        else:
            return 'No'

    # Calcular edad:
    def edad(self):
        diff = (datetime.date.today() - self.fecha_nacimiento).days
        years = str(int(diff / 365))
        return years + ' años'

    def __unicode__(self):
        return u"%s (%s)" % (self.rut, self.apellido_pat)

    def categoria(self):
        return u"%s" % self.edad_y_precio

    class Meta:
        verbose_name_plural = 'Listado Personas Inscritas'
        verbose_name = 'Persona Inscrita'
