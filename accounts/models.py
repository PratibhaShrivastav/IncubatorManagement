from django.db import models
from django.contrib.auth.models import User
from startups.models import Startup

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    startup = models.ForeignKey(Startup,related_name='startup',null=True,blank=True,on_delete=models.CASCADE,default=2)
    user_email = models.EmailField(unique = True)
    date_joined = models.DateTimeField(auto_now=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    mentor = models.BooleanField(default=False)
    
    def get_full_name(self):
        return self.user.first_name + ' ' + self.user.last_name

    def get_short_name(self):
        return self.user.first_name

    def __str__(self):
        return self.user_email

class Coffee(models.Model):
    user = models.ForeignKey(User, related_name='coffee', on_delete=models.CASCADE)
    free_coffee = models.IntegerField()
    extra_coffee = models.IntegerField()
    date = models.DateField(auto_now=True)
