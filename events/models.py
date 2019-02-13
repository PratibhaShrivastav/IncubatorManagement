from django.db import models
from startups.models import Startup

class Event(models.Model):

    CATEGORY_OPTIONS = (
        (0,'Technical'),
        (1,'Business'),
        (2,'Product'),
        (3,'IT'),
    )

    ACTIVITY_OPTIONS = (
        (0,'Interested'),
        (1,'Going'),
        (2,'Not Interested'),
    )

    startup = models.ForeignKey(Startup,related_name='event', null=True, blank=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField(auto_now=False)
    end_date = models.DateField(auto_now=False)
    category = models.IntegerField(choices=CATEGORY_OPTIONS)
    activity = models.IntegerField(choices=ACTIVITY_OPTIONS)
    location = models.TextField(default=None)
    photo = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None,null=True,blank=True)

    def __str__(self):
        return self.title
    



