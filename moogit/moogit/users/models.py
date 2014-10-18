# -*- coding: utf-8 -*-
# Import the AbstractUser model
from django.contrib.auth.models import AbstractUser

# Import the basic Django ORM models library
from django.db import models

from django.utils.translation import ugettext_lazy as _


# Subclass AbstractUser
class User(AbstractUser):

    def __unicode__(self):
        return self.username

class Venue(models.Model):
	AREA_CHOICES = (
		("NC", "North County"),
		("EC", "East County"),
		("CC", "Central"),
		("SB", "South Boy")	
	)


	venueID = models.AutoField(primary_key = True)
	venueName = models.CharField(max_length = 75)
	description = models.TextField()
	area = models.CharField(choices =  AREA_CHOICES,
							max_length = 20)
	Neighborhood = models.CharField(max_length = 75)
	dateAdded = models.DateTimeField(auto_now_add = True)
	lastSaved = models.DateTimeField(auto_now = True)
	streetAddress = models.CharField(max_length = 150)
	city = models.CharField(max_length = 150)
	# state = USPhoneNumberField()