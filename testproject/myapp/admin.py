from django.contrib import admin
from .models import Destination, Trip, Booking

# Register your models here.
admin.site.register(Destination)
admin.site.register(Trip)
admin.site.register(Booking)