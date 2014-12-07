# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('display5shows', '0004_show2_cost'),
    ]

    operations = [
        migrations.CreateModel(
            name='showOrder',
            fields=[
                ('showOrderID', models.AutoField(serialize=False, primary_key=True)),
                ('order', models.IntegerField()),
                ('bandID', models.ForeignKey(to='display5shows.Band')),
                ('show2ID', models.ForeignKey(to='display5shows.Show2')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
