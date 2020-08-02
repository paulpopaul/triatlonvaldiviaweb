# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

from django.db import models


class Region(models.Model):
    nombre = models.CharField('Nombre de la Región', max_length=50, help_text='los ríos')
    codigo = models.CharField(max_length=7, help_text='XVI, RM, etc..')

    def __unicode__(self):
        return u"(%s) Región de %s" % (self.codigo.upper(), self.nombre.title())

    class Meta:
        verbose_name = "Región de Chile"
        verbose_name_plural = "Regiones de Chile"
        ordering = ['nombre']

    def delete(self, *args, **kwargs):
        comuna = Comuna.objects.filter(region=self)
        for a in comuna:
            a.delete()
        super(Region, self).delete()


class Comuna(models.Model):
    nombre = models.CharField('Nombre de la Comuna', max_length=50, help_text='Osorno, Valdivia, Río Bueno, etc.')
    region = models.ForeignKey(Region, related_name='comuna_region')

    def __unicode__(self):
        return u"%s (%s)" % (self.nombre.title(), self.region.codigo.upper())

    class Meta:
        verbose_name = "Comuna de Chile"
        verbose_name_plural = "Comunas de Chile"
        ordering = ['nombre']
