# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('display5shows', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='show2',
            name='showVenueID',
            field=models.ForeignKey(to='display5shows.Venue'),
        ),
    ]
