# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-13 16:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SiteConfiguration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_name', models.CharField(default='djflow', max_length=255)),
            ],
            options={
                'verbose_name': 'Configuración del sitio',
            },
        ),
    ]