# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-04 07:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('osschallenge', '0033_auto_20170503_1131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='picture',
            field=models.ImageField(default=b'/home/jonas/gitty/work/oss-challenge.src/oss_challenge/osschallenge/pictures/example.jpg', upload_to=b'/home/jonas/gitty/work/oss-challenge.src/oss_challenge/osschallenge/pictures'),
        ),
    ]