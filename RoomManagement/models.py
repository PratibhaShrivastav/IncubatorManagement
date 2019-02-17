from django.db import models
from django.contrib.auth.models import User

class Room(models.Model):
    
    ROOM_CHOICES = (
        (0,'Meeting'),
        (1,'Office'),
        (2,'Conference'),
    )

    room_no = models.TextField(unique=True)
    room_type = models.IntegerField(choices=ROOM_CHOICES, default=1)

    def __str__(self):
        return self.room_no


class Seat(models.Model):
    seat_no = models.TextField(unique=True)
    booked = models.BooleanField(default=False)
    price = models.IntegerField(default=100)
    user = models.ForeignKey(User, related_name="seat_alloted", on_delete=models.CASCADE, null=True, blank=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="seats")
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.seat_no


class SeatRequest(models.Model):
    request_from = models.ForeignKey(User, unique=False, on_delete=models.CASCADE, related_name='seat_requests_sent')
    request_to = models.ForeignKey(User, unique=False,  on_delete=models.CASCADE, related_name='seat_requests_received')
    seat = models.ForeignKey(Seat, unique=False, on_delete=models.CASCADE, related_name="logs")
    approved = models.BooleanField(default=False)
    paid = models.BooleanField(default=False)
    date = models.DateField(auto_now=True)
    expired = models.BooleanField(default=False)
    

