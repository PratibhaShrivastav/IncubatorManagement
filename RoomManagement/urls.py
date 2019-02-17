from django.contrib import admin
from django.urls import path
from .views import room_detail, seat_detail, seat_request
from django.contrib.auth import views as auth_views

app_name = 'Room'

urlpatterns = [
    path('book_room/', room_detail ,name='room_list'),
    path('book_seat/<slug:pk>/', seat_detail ,name='seat_book'),
    path('seat_request/', seat_request, name='seat_request'),
]