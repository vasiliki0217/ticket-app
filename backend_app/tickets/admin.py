from django.contrib import admin
from .models import Artist, Event, Venue, User, Ticket, TicketType, Payment

admin.site.register(Artist)
admin.site.register(Event)
admin.site.register(Venue)
admin.site.register(User)
admin.site.register(Ticket)
admin.site.register(TicketType)
admin.site.register(Payment)