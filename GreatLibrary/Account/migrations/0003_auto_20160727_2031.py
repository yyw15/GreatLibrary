# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-27 12:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0002_userinfo_collectionlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='headImage',
            field=models.CharField(default='headImages/default.jpg', max_length=100),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='prevImage',
            field=models.CharField(default='headImages/default.jpg', max_length=100),
        ),
    ]
