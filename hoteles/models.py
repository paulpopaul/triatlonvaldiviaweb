# coding=utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from mapachile.models import Comuna

CHOICES_ALOJAMIENTO = (
    ('HOTEL', 'Hotel'),
    ('CABAÑA', 'Cabaña'),
    ('RESTORANT', 'Restorant'),
    ('OTROS', 'Otros'),
)


class Dato(models.Model):
    nombre = models.CharField(max_length=32)
    sub_titulo = models.CharField(max_length=32)
    tipo = models.CharField(choices=CHOICES_ALOJAMIENTO, default='CABAÑA', max_length=10)
    estrellas = models.SmallIntegerField(blank=True, null=True)
    pagina_web = models.URLField(blank=True, null=True)
    imagen = models.ImageField(upload_to='hoteles', null=True, blank=True)
    comuna = models.ForeignKey(Comuna, null=True, blank=True)
    direccion = models.CharField(max_length=64, blank=True, null=True)
    telefono = models.CharField(max_length=12, blank=True, null=True)

    url_reservas = models.URLField()
    mapa_google = models.URLField()

    def __unicode__(self):
        return u"%s (%s)" % (self.nombre, self.tipo)

    class Meta:
        verbose_name_plural = 'Alojamientos'
        verbose_name = 'Alojamiento'

    def lugar(self):
        return u"%s" % (self.comuna.nombre)

    def cantidad_estrellas(self):
        return '<i class="small material-icons yellow-text">star</i>'*self.estrellas