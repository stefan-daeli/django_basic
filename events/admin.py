from django.contrib import admin
from .models import Venue, Event, MuClubUser

# admin.site.register(Venue, VenueAdmin)
# admin.site.register(Event)
admin.site.register(MuClubUser)
@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'zip_code')
    ordering = ('name',)
    search_fields = ('name', 'address')

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    fields =(('name', 'venue'),'event_date', 'description', 'manager')
    list_display = ('name', 'event_date', 'venue')
    list_filter = ('event_date', 'venue')
    ordering = ('event_date',)
