# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('displayShow', '0003_auto_20141127_1012'),
    ]

    operations = [
        migrations.AddField(
            model_name='show',
            name='venueName',
            field=models.ForeignKey(default='default venue Name', to='displayShow.Venue'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='show',
            name='showVenueID',
            field=models.ForeignKey(to='displayShow.Show'),
        ),
    ]
