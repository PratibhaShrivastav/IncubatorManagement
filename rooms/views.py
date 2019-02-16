from django.shortcuts import render, reverse
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Room,Seat
from django.forms.models import model_to_dict
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from datetime import datetime, timedelta

@csrf_exempt
@login_required
def book_seats(request, room_no, **kwargs):
    if room_no == None:
        room_no = kwargs.get('room_number')
    
    room = Room.objects.get(number=room_no)
    startup = request.user.profile.all()[0].startup

    if request.method == "POST":
        seats = room.room_seats.all()
        for seat in seats:
            #print("Seat ",seat.id," is --> ",request.POST.get('seat_'+str(seat.id),False))
            editable = False
            if seat.is_issued:
                if seat.startup == startup:
                    seat_check = request.POST.get('seat_'+str(seat.id),False)
                    if not seat_check:
                        seat.startup = None
                        seat.is_issued = False
                        seat.end_date = datetime.today() + timedelta(days=30)
                        seat.save()
            if not seat.is_issued:
                seat_check = request.POST.get('seat_'+str(seat.id),False)
                if seat_check:
                    seat.startup = startup
                    seat.is_issued = True
                    seat.end_date = datetime.today() + timedelta(days=30)
                    seat.save()
        

    seats = room.room_seats.all()
    room = model_to_dict(room)
    startup = model_to_dict(startup)
    context = {}
    seat_list = []
    context['room'] = room
    context['startup'] = startup
    for seat in seats:
        seat_data = model_to_dict(seat)
        seat_list.append(seat_data)
    context['seats'] = seat_list

    return render(request, 'book_room.html', context=context)


@csrf_exempt
@login_required
def book_rooms(request):
    if request.method == "POST":
        room_id = request.POST.get('room_number')
        return HttpResponseRedirect("%s" % room_id)
    rooms = Room.objects.all()
    room_list = []
    for room in rooms:
        room_list.append(model_to_dict(room))
    context = {'rooms' : room_list}
    return render(request, 'room_select.html', context=context)

@csrf_exempt
@login_required
def show_seat(request, pk):
    seat = Seat.objects.get(id=pk)
    try:
        startup = seat.startup
        startup = model_to_dict(startup)
    except:
        startup = None
    
    seat = model_to_dict(seat)
    
    return render(request, 'seat_details.html', context={'seat':seat, 'startup':startup})