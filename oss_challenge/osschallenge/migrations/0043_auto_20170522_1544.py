# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-22 13:44
from __future__ import unicode_literals

from django.db import migrations
import easy_thumbnails.fields


class Migration(migrations.Migration):

    dependencies = [
        ('osschallenge', '0042_auto_20170522_1541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='picture',
            field=easy_thumbnails.fields.ThumbnailerImageField(default=b'/home/jonas/gitty/work/oss-challenge.src/osschallenge/static/osschallenge/example.jpg', upload_to=b''),
        ),
    ]