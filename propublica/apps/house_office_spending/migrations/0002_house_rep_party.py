# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-04-15 03:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('house_office_spending', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='house_rep',
            name='party',
            field=models.CharField(default=django.utils.timezone.now, max_length=5),
            preserve_default=False,
        ),
    ]