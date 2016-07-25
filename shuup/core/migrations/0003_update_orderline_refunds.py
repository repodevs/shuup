# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


def combine_refund_types(apps, schema_editor):
    OrderLine = apps.get_model("shuup", "OrderLine")

    # QUANTITY_REFUND was renamed to REFUND
    # and AMOUNT_REFUND was removed
    # convert AMOUNT_REFUND to REFUND
    for refund_line in OrderLine.objects.filter(type=8):
        refund_line.type = 6 # REFUND
        refund_line.save()


class Migration(migrations.Migration):

    dependencies = [
        ('shuup', '0002_rounding'),
    ]

    operations = [
        migrations.RunPython(combine_refund_types),
    ]
