# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'permissions': (('add_bands', 'Can add bands to the site.'), ('edit_band', 'Can edit bads on the site.'), ('delete_band', 'Can delete bands from the site.'), ('add_show', 'Can add shows to the site.'), ('edit_show', 'Can edit shows on the site.'), ('delete_show', 'Can delete shows from the site.'), ('add_venue', 'Can add venues to the site.'), ('edit_venue', 'Can edit venues on the site.'), ('delete_venue', 'Can delete vnues from the site.'), ('add_mod', 'Can add users with mod permissions.'), ('delete_mod', 'Can delte users with mod permissions'))},
        ),
    ]
