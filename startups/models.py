from django.db import models

class Startup(models.Model):

    name = models.CharField(max_length=50)
    motto = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='Startup' ,null=True,blank=True)
    worth = models.IntegerField()

    def __str__(self):
        return self.name

class StartupLog(models.Model):

    startup =  models.ForeignKey(Startup,related_name='log', on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    update_title = models.CharField(max_length=50)
    update_description = models.TextField()
    photo = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None,null=True,blank=True)