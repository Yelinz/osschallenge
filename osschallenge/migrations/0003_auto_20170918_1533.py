# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-09-18 13:33
from __future__ import unicode_literals

from django.db import migrations
import django_markdown.models


class Migration(migrations.Migration):

    dependencies = [
        ('osschallenge', '0002_remove_task_mentors'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=django_markdown.models.MarkdownField(max_length=150),
        ),
    ]
