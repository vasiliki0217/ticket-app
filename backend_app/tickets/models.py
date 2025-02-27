from django.db import models


class Artist(models.Model):
    id = models.AutoField(primary_key=True)  
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=50, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    website = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'artists'


class EventCategory(models.Model):
    id = models.AutoField(primary_key=True)
    category_name = models.CharField(unique=True, max_length=50)

    class Meta:
        db_table = 'event_categories'


class Venue(models.Model):
    id = models.AutoField(primary_key=True)
    venue_name = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    street_number = models.CharField(max_length=10)
    postal_code = models.CharField(max_length=20)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

    class Meta:
        db_table = 'venues'


class Event(models.Model): 
    id = models.AutoField(primary_key=True)
    event_category = models.ForeignKey(EventCategory, on_delete=models.PROTECT)
    starting_time = models.DateTimeField()
    finish_time = models.DateTimeField()
    doors_open_at = models.TimeField()
    venue = models.ForeignKey(Venue, on_delete=models.PROTECT)
    capacity = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    artist = models.ForeignKey(Artist, on_delete=models.PROTECT)

    class Meta:
        db_table = 'events'


class User(models.Model): 
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    password = models.TextField()
    email = models.CharField(unique=True, max_length=100)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'users'


class TicketType(models.Model):
    id = models.AutoField(primary_key=True)
    event = models.ForeignKey(Event, on_delete=models.PROTECT)
    category = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    capacity_of_category = models.IntegerField()

    class Meta:
        db_table = 'ticket_types'


class Ticket(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    event = models.ForeignKey(Event, on_delete=models.PROTECT)
    purchase_date = models.DateTimeField(blank=True, null=True)
    status = models.TextField(blank=True, null=True)
    ticket_type = models.ForeignKey(TicketType, on_delete=models.PROTECT)

    class Meta:
        db_table = 'tickets'


class Payment(models.Model): 
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    ticket = models.ForeignKey(Ticket, on_delete=models.PROTECT)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'payments'
