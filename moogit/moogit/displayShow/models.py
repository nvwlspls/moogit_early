from django.db import models

from localflavor.us.forms import USPhoneNumberField, USStateSelect, USZipCodeField



# Create your models here.
class Venue(models.Model):
    AREA_CHOICES = (
        ("NC", "North County"),
        ("EC", "East County"),
        ("CC", "Central"),
        ("SB", "South Boy") 
    )


    venueID = models.AutoField(primary_key = True)
    venueName = models.CharField(max_length = 75,
                                default = "Venue Name")
    description = models.TextField()
    area = models.CharField(choices =  AREA_CHOICES,
                            max_length = 20)
    neighborhood = models.CharField(max_length = 75,
                                        default = "Neighborhood")
    venueDateAdded = models.DateTimeField(auto_now_add = True)
    venueLastMod = models.DateTimeField(auto_now = True)
    streetAddress = models.CharField(max_length = 150,
                                        default = "Street Address")
    city = models.CharField(max_length = 150,
                                default = "City")
    state = USStateSelect()
    zipCode = USZipCodeField()
    phone = USPhoneNumberField()
    conFirstName = models.CharField(max_length = 100,
                                    default = "First Name")
    conLastName = models.CharField(max_length = 100,
                                    default  = "Last Name")
    conEmail = models.EmailField(max_length = 100,
                                default = "email@email.com")

class Band(models.Model):
    bandID = models.AutoField(primary_key = True)
    bandName = models.CharField(max_length = 200,
                                default = "Band Name")
    homeTown = models.CharField(max_length = 100,
                                default = "Home Town")
    homeState = USStateSelect()
    #TODO: Add a genre selection field
    genre = models.CharField(max_length = 75 )
    bandDateAdded = models.DateTimeField(auto_now_add = True)
    bandDateMod = models.DateTimeField(auto_now = True)

class Show(models.Model):
    showID = models.AutoField(primary_key = True)
    showVenueID = models.ForeignKey("Band")
    #TODO add sep. date and time fields
    Date = models.DateTimeField()
    band1 = models.CharField(max_length = 150,
                            default = "Band 1")
    band2 = models.CharField(max_length = 150,
                            default = "Band 2")
    band3 = models.CharField(max_length = 150,
                            default = "Band 3")
    band4 = models.CharField(max_length = 150,
                            default = "Band 4")
    bandsExtra = models.TextField()
    showDateAdded = models.DateTimeField( auto_now_add = True)
    showDateMod = models.DateTimeField( auto_now = True )
