from django.contrib import admin
from .models import Venue, Event, MuClubUser

admin.site.register(Venue)
admin.site.register(Event)
admin.site.register(MuClubUser)