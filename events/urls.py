from django.contrib import admin
from django.urls import path
from .views import CreateEvent
from django.contrib.auth import views as auth_views
from django import views

app_name = 'events'

urlpatterns = [
    path('create/',CreateEvent.as_view(),name='create-event'),
]