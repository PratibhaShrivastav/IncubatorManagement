from django.contrib import admin
from django.urls import path,include
from .views import Startup_Log, CreateStartup, startup_success

app_name = 'startups'

urlpatterns = [
    path('<int:pk>/create-log/',Startup_Log.as_view(),name='create-log'),
    path('verify-startup/',CreateStartup.as_view(),name='verify-startup'),
    path('verify-startup/success/',startup_success,name='verify-success'),
]
