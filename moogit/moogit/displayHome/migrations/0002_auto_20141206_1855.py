# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('displayHome', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='show2',
            name='showOrderID',
        ),
        migrations.AddField(
            model_name='showorder',
            name='showID',
            field=models.ForeignKey(default=1, to='displayHome.Show2'),
            preserve_default=False,
        ),
    ]
