# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-10-10 11:11
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('osschallenge', '0006_auto_20171009_1639'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='approved_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
