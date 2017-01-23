# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-01-23 11:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shuup', '0025_product_variation_ordering'),
        ('campaigns', '0007_add_excluded_categories'),
    ]

    operations = [
        migrations.CreateModel(
            name='FreeShippingMethodLine',
            fields=[
                ('basketlineeffect_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='campaigns.BasketLineEffect')),
                ('methods', models.ManyToManyField(to='shuup.ShippingMethod', verbose_name='shipping method')),
            ],
            options={
                'abstract': False,
            },
            bases=('campaigns.basketlineeffect',),
        ),
    ]
