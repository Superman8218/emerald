# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-09-07 18:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('data', '0008_auto_20160903_2341'),
    ]

    operations = [
        migrations.CreateModel(
            name='Opportunity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Account')),
                ('fbomaster', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.FboMaster')),
            ],
        ),
    ]