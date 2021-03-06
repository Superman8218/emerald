# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-01-12 18:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FpdsMaster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agency', models.CharField(max_length=50)),
                ('mod_number', models.IntegerField()),
                ('referenced_idvid_agency_name', models.CharField(max_length=100)),
                ('referenced_idvid_agency_id', models.CharField(max_length=6)),
                ('referenced_idvid_mod_number', models.IntegerField()),
                ('piid', models.CharField(max_length=50)),
                ('modification_number', models.CharField(max_length=25)),
                ('referenced_piid', models.CharField(max_length=50)),
                ('transaction_number', models.IntegerField()),
                ('agency_id', models.CharField(max_length=4)),
                ('solicitation_identifier', models.CharField(max_length=25)),
                ('referenced_idv_modification_number', models.CharField(max_length=25)),
                ('referenced_idv_agency_id', models.CharField(max_length=4)),
                ('date_signed', models.DateField()),
                ('effective_date', models.DateField()),
                ('current_completion_date', models.DateField()),
                ('ultimate_completion_date', models.DateField()),
                ('idv_last_date', models.DateField()),
                ('ultimate_contract_value', models.DecimalField(decimal_places=2, max_digits=20)),
                ('current_contract_value', models.DecimalField(decimal_places=2, max_digits=20)),
                ('dollars_obligation', models.DecimalField(decimal_places=2, max_digits=20)),
                ('contracting_agency', models.CharField(max_length=4)),
                ('contracting_office_code', models.CharField(max_length=4)),
                ('funding_agency_id', models.CharField(max_length=4)),
                ('funding_office_code', models.CharField(max_length=6)),
                ('foreign_funding', models.CharField(max_length=1)),
                ('url_of_program', models.URLField(max_length=100)),
                ('who_can_use', models.CharField(max_length=255)),
                ('maximum_order_limit', models.DecimalField(decimal_places=2, max_digits=22)),
                ('fee_for_use_of_service', models.CharField(max_length=3)),
                ('fixed_fee_value', models.CharField(max_length=6)),
                ('fee_range_lower_value', models.IntegerField()),
                ('fee_range_upper_value', models.IntegerField()),
                ('ordering_procedure', models.TextField()),
                ('fee_paid_for_use_of_service', models.DecimalField(decimal_places=2, max_digits=22)),
                ('email_address', models.EmailField(max_length=254)),
                ('type_of_contract_pricing', models.CharField(max_length=1)),
            ],
        ),
    ]
