# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('venueID', models.AutoField(serialize=False, primary_key=True)),
                ('venueName', models.CharField(max_length=75)),
                ('description', models.TextField()),
                ('area', models.CharField(max_length=20, choices=[(b'NC', b'North County'), (b'EC', b'East County'), (b'CC', b'Central'), (b'SB', b'South Boy')])),
                ('Neighborhood', models.CharField(max_length=75)),
                ('dateAdded', models.DateTimeField(auto_now_add=True)),
                ('lastSaved', models.DateTimeField(auto_now=True)),
                ('streetAddress', models.CharField(max_length=150)),
                ('city', models.CharField(max_length=150)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
