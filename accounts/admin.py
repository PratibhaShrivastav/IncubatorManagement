from django.contrib import admin
from .models import Profile,Coffee,CoffeeLog

admin.site.register(Profile)
admin.site.register(Coffee)
admin.site.register(CoffeeLog)