from django.contrib import admin
from django.urls import path
from .views import CreateEvent, event_all, show_event
from django.contrib.auth import views as auth_views
from django import views

app_name = 'events'

urlpatterns = [
    path('create/',CreateEvent.as_view(),name='create-event'),
    path('all/',event_all,name='all_events'),
    path('<int:pk>/',show_event, name="show_event"),
]