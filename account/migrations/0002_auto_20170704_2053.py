# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-04 19:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailconfirmation',
            name='status',
            field=models.CharField(default='sent', max_length=30),
        ),
    ]