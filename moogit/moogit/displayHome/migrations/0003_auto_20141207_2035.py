# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('displayHome', '0002_auto_20141206_1855'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='showorder',
            options={'ordering': ['order']},
        ),
        migrations.AddField(
            model_name='show2',
            name='orders',
            field=models.ManyToManyField(related_name=b'orders', to='displayHome.showOrder'),
            preserve_default=True,
        ),
    ]
