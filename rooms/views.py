from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Room
from django.forms.models import model_to_dict
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
@login_required
def book_seats(request, room_no):

    room = Room.objects.get(number=room_no)
    
    if request.method == "POST":
        print("Book")

    seats = room.room_seats.all()
    room = model_to_dict(room)
    context = {}
    seat_list = []
    context['room'] = room
    for seat in seats:
        seat_data = model_to_dict(seat)
        seat_list.append(seat_data)
    context['seats'] = seat_list

    return render(request, 'book_room.html', context=context)

    
