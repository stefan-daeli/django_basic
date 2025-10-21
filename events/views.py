from django.shortcuts import render, redirect
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from django.http import HttpResponseRedirect
from .models import Event, Venue
from .forms import VenueForm, EventForm
from django.http import HttpResponse
import csv

def venue_csv(request):
    response = HttpResponse(content_type='text/csv') #use csv not plain
    response['Content-Disposition'] = 'attachment; filename=venues.csv'
    # create a csv writer
    writer = csv.writer(response)
    venues = Venue.objects.all()
    # add column headings to the csv file
    writer.writerow(['Venue Name','Address','Zip Code','Phone','Web','Email'])
    for venue in venues:
        writer.writerow(
            [venue.name ,
             venue.address,
             venue.zip_code,
             venue.phone,
             venue.web,
             venue.email_address]
        )
    return response
    

# generate text file venue list
def venue_text(request):
    response = HttpResponse(content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename=venues.txt'
    # designate the model
    venues = Venue.objects.all()
    # create blank list
    lines = []
    # loop thu and output
    for venue in venues:
        lines.append(
            f'Venue Name : {venue}\n\nAddress : {venue.address}\nZip Code : {venue.zip_code}\nPhone : {venue.phone}\nWeb : {venue.web}\nEmail : {venue.email_address}\n\n' ,
        )
    # lines = ["This is line 1\n",
    #          "This is line 2\n",
    #          "This is line 3\n"]
    
    
    # write to text file
    response.writelines(lines)
    return response

# Delete an Venue
def delete_venue(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    venue.delete()
    return redirect('list-venues')
# Delete an Event
def delete_event(request, event_id):
    event = Event.objects.get(pk=event_id)
    event.delete()
    return redirect('list-events')

def update_event(request, event_id):
    event = Event.objects.get(pk=event_id)
    form = EventForm(request.POST or None, instance=event)
    if form.is_valid():
        form.save()
        return redirect('list-events')
    return render(request, 'events/update_event.html',
                    {'event': event,
                     'form': form})

def add_event(request):
    submitted = False
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_event?submitted=True')
    else:
        form = EventForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'events/add_event.html', {'form' : form, 'submitted': submitted})

def update_venue(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    form = VenueForm(request.POST or None, instance=venue)
    if form.is_valid():
        form.save()
        return redirect('list-venues')
    return render(request, 'events/update_venue.html',
                    {'venue': venue,
                     'form': form})

def search_venues(request):
    if request.method == "POST":
        searched = request.POST.get('searched')
        venues = Venue.objects.filter(name__icontains=searched)
        return render(request, 
                      'events/search_venues.html',
                      {'searched': searched,
                       'venues': venues})
    else:
        return render(request, 
                  'events/search_venues.html',
                  {})

def show_venue(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    return render(request, 'events/show_venue.html',
                    {'venue': venue})

def list_venues(request):
    # venue_list = Venue.objects.all().order_by('name')
    venue_list = Venue.objects.all().order_by('?') #random_order
    return render(request, 'events/venue_list.html',
                    {'venue_list': venue_list})

def add_venue(request):
    submitted = False
    if request.method == "POST":
        form = VenueForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_venue?submitted=True')
    else:
        form = VenueForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'events/add_venue.html', {'form' : form, 'submitted': submitted})

def all_events(request):
    # event_list = Event.objects.all().order_by('-name')
    # event_list = Event.objects.all().order_by('name')
    # event_list = Event.objects.all().order_by('name', 'venue')
    event_list = Event.objects.all().order_by('event_date')
    return render(request, 'events/event_list.html',
                    {'event_list': event_list})

def home(request, year=datetime.now().year, 
         month=datetime.now().strftime('%B')):
    name = "John"
    month = month.capitalize()
    # convert month from name to number
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)
    # create a calendar
    cal = HTMLCalendar().formatmonth(
        year, 
        month_number)
    
    # get current year
    now = datetime.now()
    current_year = now.year

    # get current time
    current_time = now.strftime('%I:%M:%S %p')
    return render(request, 'events/home.html', 
                  {'name' : name,
                   'year' : year,
                   'month' : month,
                   'month_number' : month_number,
                   'cal' : cal,
                   'current_year' : current_year,
                   'current_time' : current_time
                   })
