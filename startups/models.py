from django.db import models
from django.http import HttpResponse
from django.contrib.auth.models import User


class Startup(models.Model):

    STATUS = (
        (0, 'PENDING'),
        (1, 'ACCEPTED'),
        (2, 'REJECTED'),
    )
    
    name = models.CharField(max_length=50)
    description = models.TextField(default = "")
    motto = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='images/startups/logo/',default='images/startups/logo/logo.png')
    worth = models.IntegerField()
    email = models.CharField(max_length=50)
    image1 = models.ImageField(null=True,blank=True,upload_to=None, height_field=None, width_field=None, max_length=None)
    image2 = models.ImageField(null=True,blank=True,upload_to=None, height_field=None, width_field=None, max_length=None)
    image3 = models.ImageField(null=True,blank=True,upload_to=None, height_field=None, width_field=None, max_length=None)
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return self.name
    

class StartupLog(models.Model):

    startup =  models.ForeignKey(Startup,related_name='log', on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    update_title = models.CharField(max_length=50)
    update_description = models.TextField()
    sentiment = models.IntegerField(default=0)
    photo = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None,null=True,blank=True)


class Mentoring(models.Model):
    
    STATUS = (
        (0, "PENDING"),
        (1, "ACCEPTED"),
        (2, "REJECTED"),
    )
    
    startup = models.ForeignKey(Startup, related_name="mentor", on_delete=models.CASCADE)
    mentor = models.ForeignKey(User, related_name="mentoring_startups", on_delete=models.CASCADE)
    status = models.IntegerField(default=0, choices=STATUS)
    action = models.IntegerField(default=1)

    def __str__(self):
        return self.startup.name + ' mentored by ' + self.mentor.username
