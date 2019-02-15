from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Room,Seat
from django.forms.models import model_to_dict
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
@login_required
def book_seats(request, room_no):

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
                        seat.save()
            if not seat.is_issued:
                seat_check = request.POST.get('seat_'+str(seat.id),False)
                if seat_check:
                    seat.startup = startup
                    seat.is_issued = True
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

    
