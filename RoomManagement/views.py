from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
from .models import Room, Seat, SeatRequest
from django.contrib.auth.models import User
from datetime import timedelta

@csrf_exempt
def room_detail(request):
    if request.method == "POST":
        room_no=request.POST.get('room_num')
        
        #Getting details of room
        room = Room.objects.get(room_no=room_no)
        seats = room.seats.all()
        
        seat_list = []
        for seat in seats:
            seat_list.append(model_to_dict(seat))

        room = model_to_dict(room)
        context = {'room':room}
        context['seats'] = seat_list
        return render(request, "rooms/room_detail.html", context=context)

    #Getting all Rooms
    rooms = Room.objects.all()
    #Converting into dictionary
    room_list = []
    for room in rooms:
        room_list.append(model_to_dict(room))
    context = {'rooms': room_list}
    return render(request, "rooms/room_list.html", context=context)

@csrf_exempt
def seat_detail(request, pk):
    if request.method == "POST":
        seat = Seat.objects.get(seat_no=pk)
        seat = model_to_dict(seat)
        users = User.objects.all()
        user_list = []

        for user in users:
            user_list.append(model_to_dict(user))

        return render(request, "seat/book_seat.html", context={'seat':seat,'users':user_list})
    return render(request, "seat/book_seat.html")

@csrf_exempt
def seat_request(request):
    if request.method == "POST":
        seat_no = request.POST.get('seat_no')
        userpk = request.POST.get('userid')
        #pdb.set_trace()
        seat = Seat.objects.get(seat_no=seat_no)
        user = User.objects.get(id=userpk)
        request_by = request.user
        if not request_by == user:
            print(request_by.id,'->',user.id)
            seat_request = SeatRequest(seat=seat, request_from=request_by, request_to=user)
            seat_request.save()
        else:
            seat_request = SeatRequest(seat=seat, request_from=request_by, request_to=user, approved=True)
            seat_request.save()
            seat.booked = True
            seat.user = request_by
            seat.date = seat.date + timedelta(days=30)
            seat.save()

        user = model_to_dict(user)

        return render(request, "seat/seat_book_detail.html", context={'user':user})
    return render(request, "seat/seat_book_detail.html")


