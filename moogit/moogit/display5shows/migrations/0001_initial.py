# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
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
            name='Show2',
            fields=[
                ('show2ID', models.AutoField(serialize=False, primary_key=True)),
                ('Date', models.DateField()),
                ('Time', models.TimeField()),
                ('DateTimeAdded', models.DateTimeField(auto_now_add=True)),
                ('DateTimeMod', models.DateTimeField(auto_now=True)),
                ('bandExtraTesxt', models.TextField()),
                ('bands', models.ManyToManyField(related_name=b'bands', to='display5shows.Band')),
                ('showVenueID', models.ForeignKey(to='display5shows.Band')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('venueID', models.AutoField(serialize=False, primary_key=True)),
                ('venueName', models.CharField(default=b'Venue Name', max_length=75)),
                ('description', models.TextField()),
                ('area', models.CharField(max_length=20, choices=[(b'NC', b'North County'), (b'EC', b'East County'), (b'CC', b'Central'), (b'SB', b'South Boy')])),
                ('neighborhood', models.CharField(default=b'Neighborhood', max_length=75)),
                ('venueDateAdded', models.DateTimeField(auto_now_add=True)),
                ('venueLastMod', models.DateTimeField(auto_now=True)),
                ('streetAddress', models.CharField(default=b'Street Address', max_length=150)),
                ('city', models.CharField(default=b'City', max_length=150)),
                ('conFirstName', models.CharField(default=b'First Name', max_length=100)),
                ('conLastName', models.CharField(default=b'Last Name', max_length=100)),
                ('conEmail', models.EmailField(default=b'email@email.com', max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
