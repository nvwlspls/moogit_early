# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('display5shows', '0008_show2_showorderid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='showorder',
            name='show2ID',
        ),
    ]
