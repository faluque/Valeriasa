# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-26 13:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuentas', '0006_auto_20190326_1009'),
    ]

    operations = [
        migrations.AddField(
            model_name='ctacte',
            name='nro_inquilino',
            field=models.IntegerField(blank=True, null=True, unique=True),
        ),
    ]
