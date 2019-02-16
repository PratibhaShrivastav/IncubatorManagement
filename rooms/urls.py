from django.contrib import admin
from django.urls import path
from .views import book_seats, book_rooms, show_seat
from django.contrib.auth import views as auth_views

app_name = 'rooms'

urlpatterns = [
    path('book/<int:room_no>/', book_seats,name='book_seat'),
    path('book/', book_rooms,name='book_room'),
    path('show/seat/<int:pk>/', show_seat, name='show_seat'),
]