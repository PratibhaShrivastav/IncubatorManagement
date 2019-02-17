from django.contrib import admin
from .models import Startup,StartupLog, Mentoring

admin.site.register(Startup)
admin.site.register(StartupLog)
admin.site.register(Mentoring)