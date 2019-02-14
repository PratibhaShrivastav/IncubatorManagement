from django.db import models
from startups.models import Startup


class Room(models.Model):

    ROOM_CHOICES = (
        (0,'Meeting'),
        (1,'Office'),
        (2,'Conference'),
    )

    room_type = models.IntegerField(choices=ROOM_CHOICES)
    seats = models.IntegerField()
    rent = models.IntegerField()
    number = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.number


class Seat(models.Model):

    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    startup = models.ForeignKey(Startup, on_delete=models.CASCADE, null=True, blank=True)
    is_issued = models.BooleanField(default=False)

    def __str__(self):
        return 'Seat no. ' + str(self.id)