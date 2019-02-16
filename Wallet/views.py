from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
from django.contrib.auth.models import User
from datetime import timedelta
from .models import Wallet
from accounts.models import Coffee, CoffeeLog
from RoomManagement.models import Seat, SeatRequest
from django.contrib.auth.decorators import login_required


@login_required
def get_wallet(request):

    try:
        wallet = Wallet.objects.get(user=request.user)
    except:
        wallet = Wallet(user=request.user)
        wallet.save()
    coffees = CoffeeLog.objects.filter(user=request.user, order_complete=True).count()
    wallet.total_coffee = coffees*25
    seat_rent = SeatRequest.objects.all().filter(request_to=request.user, approved=True, paid=False).count()
    wallet.total_rent = seat_rent*100
    wallet.save()
    wallet = model_to_dict(wallet)

    return render(request, "wallet.html", context={'wallet':wallet})