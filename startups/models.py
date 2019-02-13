from django.db import models

class Startup(models.Model):

    name = models.CharField(max_length=50)
    motto = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='Startup' ,null=True,blank=True)
    worth = models.IntegerField()

    def __str__(self):
        return self.name