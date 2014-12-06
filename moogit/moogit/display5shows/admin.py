from django.contrib import admin

# Register your models here.
from models import Venue, Show2, Band

admin.site.register(Show2)
admin.site.register(Band)
admin.site.register(Venue)