from django.db import models

# Create your models here.

class Room(models.Model):

    ROOM_CHOICES = (
        (0,'Meeting'),
        (1,'Office'),
        (2,'Conference'),
    )

    type = models.IntegerField(choices=ROOM_CHOICES)
    seats = models.IntegerField()
    rent = models.IntegerField()
    number = models.IntegerField()