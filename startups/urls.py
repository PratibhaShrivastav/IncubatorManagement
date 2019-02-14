from django.contrib import admin
from django.urls import path,include
from .views import Startup_Log

app_name = 'startups'

urlpatterns = [
    path('<int:pk>/create-log/',Startup_Log.as_view(),name='create-log'),
]
