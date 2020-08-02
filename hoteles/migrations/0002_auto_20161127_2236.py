# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-28 01:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hoteles', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dato',
            options={'verbose_name': 'Alojamiento', 'verbose_name_plural': 'Alojamientos'},
        ),
        migrations.AlterField(
            model_name='dato',
            name='comuna',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mapachile.Comuna'),
        ),
    ]
