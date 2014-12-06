# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('displayShow', '0004_auto_20141127_1019'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='show',
            name='venueName',
        ),
    ]
