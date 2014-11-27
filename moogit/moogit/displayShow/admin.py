from django.contrib import admin

# Register your models here.
from models import Venue, Show, Band

admin.site.register(Show)
admin.site.register(Band)
admin.site.register(Venue)