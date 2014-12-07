# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('display5shows', '0005_showorder'),
    ]

    operations = [
        migrations.AddField(
            model_name='show2',
            name='showOrderID',
            field=models.ForeignKey(default=0, to='display5shows.showOrder'),
            preserve_default=False,
        ),
    ]
