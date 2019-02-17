from django.contrib import admin
from .models import Room, Seat, SeatRequest

admin.site.register(Room)
admin.site.register(Seat)
admin.site.register(SeatRequest)