# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('displayShow', '0002_auto_20141019_2130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='show',
            name='showVenueID',
            field=models.ForeignKey(to='displayShow.Venue'),
        ),
    ]
