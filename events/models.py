from django.db import models
from startups.models import Startup

class Event(models.Model):

    CATEGORY_OPTIONS = (
        (0,'Meeting'),
        (1,'Conference'),
        (2,'Seminar'),
        (3,'Hackathon'),
    )

    startup = models.ForeignKey(Startup,related_name='event', null=True, blank=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField(auto_now=False)
    end_date = models.DateField(auto_now=False)
    category = models.IntegerField(choices=CATEGORY_OPTIONS)
    location = models.TextField(default=None)
    photo = models.ImageField(upload_to='images/events/', default='images/events/codergirl.png', height_field=None, width_field=None, max_length=None,null=True,blank=True)

    def __str__(self):
        return self.title
    



