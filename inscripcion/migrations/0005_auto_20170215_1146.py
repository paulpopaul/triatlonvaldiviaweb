# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-15 14:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inscripcion', '0004_auto_20170215_1145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='rut',
            field=models.CharField(help_text='12345678-5', max_length=18, verbose_name='RUT'),
        ),
    ]