# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('displayShow', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Band',
            fields=[
                ('bandID', models.AutoField(serialize=False, primary_key=True)),
                ('bandName', models.CharField(default=b'Band Name', max_length=200)),
                ('homeTown', models.CharField(default=b'Home Town', max_length=100)),
                ('genre', models.CharField(max_length=75)),
                ('bandDateAdded', models.DateTimeField(auto_now_add=True)),
                ('bandDateMod', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Show',
            fields=[
                ('showID', models.AutoField(serialize=False, primary_key=True)),
                ('Date', models.DateTimeField()),
                ('band1', models.CharField(default=b'Band 1', max_length=150)),
                ('band2', models.CharField(default=b'Band 2', max_length=150)),
                ('band3', models.CharField(default=b'Band 3', max_length=150)),
                ('band4', models.CharField(default=b'Band 4', max_length=150)),
                ('bandsExtra', models.TextField()),
                ('showDateAdded', models.DateTimeField(auto_now_add=True)),
                ('showDateMod', models.DateTimeField(auto_now=True)),
                ('showVenueID', models.ForeignKey(to='displayShow.Band')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RenameField(
            model_name='venue',
            old_name='dateAdded',
            new_name='venueDateAdded',
        ),
        migrations.RenameField(
            model_name='venue',
            old_name='lastSaved',
            new_name='venueLastMod',
        ),
    ]
