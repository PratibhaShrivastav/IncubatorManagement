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
    coffees = CoffeeLog.objects.filter(user=request.user, order_complete=False).count()
    wallet.coffee_total = coffees*25
    seat_rent = SeatRequest.objects.all().filter(request_to=request.user, paid=False).count()
    wallet.rent_total = seat_rent*100
    
    if wallet.balance > wallet.coffee_total:
        wallet.balance = wallet.balance - wallet.coffee_total
        wallet.coffee_total = 0
    if wallet.balance > wallet.rent_total:
        wallet.balance = wallet.balance - wallet.rent_total
        wallet.rent_total = 0
    
    wallet.save()
    wallet = model_to_dict(wallet)

    return render(request, "wallet.html", context={'wallet':wallet})