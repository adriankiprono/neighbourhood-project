# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2020-01-20 08:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('neighbour', '0007_neighbourhood_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='neighbourhood',
            name='post',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='neighbourhood',
        ),
        migrations.AddField(
            model_name='neighbourhood',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='neighbour.Profile'),
        ),
    ]