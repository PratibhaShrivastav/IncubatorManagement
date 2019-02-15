from django.contrib import admin
from django.urls import path
from .views import book_seats
from django.contrib.auth import views as auth_views

app_name = 'rooms'

urlpatterns = [
    path('book/<int:room_no>/', book_seats,name='book_room'),
]