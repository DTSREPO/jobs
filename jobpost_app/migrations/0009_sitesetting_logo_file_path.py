# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-10-17 06:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobpost_app', '0008_sitesetting'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitesetting',
            name='logo_file_path',
            field=models.CharField(default='', max_length=300),
        ),
    ]
