# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('display5shows', '0002_auto_20141206_1601'),
    ]

    operations = [
        migrations.AddField(
            model_name='show2',
            name='age',
            field=models.IntegerField(default=99),
            preserve_default=False,
        ),
    ]
