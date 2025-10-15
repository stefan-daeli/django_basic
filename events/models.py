from django.db import models

class Venue(models.Model):
    name = models.CharField('Venue Name', max_length=120)
    address = models.CharField(max_length=300)
    zip_code = models.CharField('Zip Code', max_length=12)
    phone = models.CharField('Contact Phone', max_length=20, blank=True)
    phone = models.URLField('Website Address', blank=True)
    email_address = models.EmailField('Email Address', blank=True)
    
    def __str__(self):
        return self.name

class MuClubUser(models.Model):
    first_name = models.CharField('First Name', max_length=60)
    last_name = models.CharField('Last Name', max_length=60)
    email = models.EmailField('User Email')
    
    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Event(models.Model):
    name = models.CharField('Event Name', max_length=120)
    event_date = models.DateTimeField('Event Date')
    venue = models.ForeignKey(Venue, blank=True, null=True, on_delete=models.CASCADE)
    # venue = models.CharField(max_length=120)
    manager = models.CharField(max_length=60)
    description = models.TextField(blank=True)
    attendees = models.ManyToManyField(MuClubUser, blank=True)

    def __str__(self):
        return self.name
