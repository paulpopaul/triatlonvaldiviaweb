# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-15 00:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inscripcion', '0002_auto_20161214_2136'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoriaacompetir',
            name='distancia',
            field=models.CharField(blank=True, choices=[('MED', 'Media'), ('ALL', 'Entera')], max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='persona',
            name='edad_y_precio',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='categoria_persona', to='inscripcion.CategoriaACompetir'),
        ),
    ]
