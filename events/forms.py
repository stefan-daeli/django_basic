from django import forms 
from django.forms import ModelForm
from .models import Venue
from .models import Event

# create a venue form
class VenueForm(ModelForm):
    # inner class from class VenueForm
    class Meta:
        model = Venue
        # fields = "__all__"
        fields = ('name', 'address', 'zip_code', 'phone', 'web', 'email_address')
        labels = {
            'name' : '',
            'address' : '',
            'zip_code' : '',
            'phone' : '',
            'web' : '',
            'email_address' : '',
        }
        widgets = {
            'name' : forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Venue Name'}),
            'address' : forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Address'}),
            'zip_code' : forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Zip Code'}),
            'phone' : forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Phone Number'}),
            'web' : forms.URLInput(attrs={'class': 'form-control', 'placeholder' : 'Website'}),
            'email_address' : forms.EmailInput(attrs={'class': 'form-control', 'placeholder' : 'Email Address'}),
            
        }

class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ('name', 'event_date', 'venue', 'manager', 'description', 'attendees')
        labels = {
            'name' : '',
            'event_date' : 'YYYY-MM-DD HH:MM:SS',
            'venue' : 'Venue',
            'manager' : 'Manager',
            'description' : '',
            'attendees' : 'Attendees',
        }
        widgets = {
            'name' : forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Event Name'}),
            'event_date' : forms.TextInput(attrs={'type' : 'datetime-local', 'class': 'form-control', 'placeholder' : 'Event Date'}),
            'venue' : forms.Select(attrs={'class': 'form-select'}),
            'manager' : forms.Select(attrs={'class': 'form-select'}),
            'description' : forms.Textarea(attrs={'class': 'form-control', 'placeholder' : 'Event Description', 'rows':3}),
            'attendees' : forms.SelectMultiple(attrs={'class': 'form-select'}),
        }