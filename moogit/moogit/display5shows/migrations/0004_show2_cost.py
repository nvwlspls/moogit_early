# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('display5shows', '0003_show2_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='show2',
            name='cost',
            field=models.DecimalField(default=99.99, max_digits=5, decimal_places=2),
            preserve_default=False,
        ),
    ]
