# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2020-01-20 07:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neighbour', '0004_auto_20200120_0957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='neighbourhood',
            name='health_tell',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='neighbourhood',
            name='police_number',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
    ]