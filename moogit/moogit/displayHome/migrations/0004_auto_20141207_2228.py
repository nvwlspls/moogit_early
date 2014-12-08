# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('displayHome', '0003_auto_20141207_2035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='showorder',
            name='bandID',
            field=models.ForeignKey(related_name=b'bandIDOrder', to='displayHome.Band'),
        ),
        migrations.AlterField(
            model_name='showorder',
            name='showID',
            field=models.ForeignKey(related_name=b'showIDOrder', to='displayHome.Show2'),
        ),
    ]
