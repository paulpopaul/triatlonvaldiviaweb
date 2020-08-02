# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-15 14:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inscripcion', '0006_auto_20170215_1148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='edad_y_precio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categoria_persona', to='inscripcion.CategoriaACompetir'),
        ),
        migrations.AlterField(
            model_name='persona',
            name='rut',
            field=models.CharField(help_text='12345678-5', max_length=15, verbose_name='RUT'),
        ),
    ]
