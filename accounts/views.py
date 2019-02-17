from django.shortcuts import render, reverse
from django.contrib.auth.models import User
from django.views.generic import CreateView,ListView
from .forms import UserForm
from django.urls import reverse_lazy
from RoomManagement.models import Seat, SeatRequest
from .models import Profile as Profile,Coffee,CoffeeLog,Startup
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate
from django.core import serializers
from django.forms.models import model_to_dict
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from startups.models import Mentoring
from django.shortcuts import get_object_or_404



class SignUp(CreateView):
    model = User
    form_class = UserForm
    template_name = 'signup.html'
    success_url = reverse_lazy('accounts:login')

    def form_valid(self, form):
        user = form.save(commit = False)
        user.is_active = 1
        user.save()
        return super().form_valid(form)

class CreateProfile(CreateView):
    model = Profile
    template_name = 'create_profile.html'
    success_url = reverse_lazy('home')
    fields = ('user_email',)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        startups = Startup.objects.all()
        
        startup_list = []
        for startup in startups:
            startup_list.append(model_to_dict(startup))
        
        context['startups'] = startup_list
        return context

    def form_valid(self, form):
        profile = form.save(commit=False)
        startup_id = self.request.POST.get('startup')
        if startup_id == "-1":
            profile.mentor = True
            profile.startup = None
        else:
            startup = Startup.objects.get(id=startup_id)
            profile.startup = startup
        profile.user = self.request.user
        return super().form_valid( form)


def logout(request):
    auth_logout(request)
    return HttpResponseRedirect(reverse('home'))

@csrf_exempt
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username=username, password=password)
        if user:
            auth_login(request, user)
            if Profile.objects.filter(user=request.user).count() == 0:
                return HttpResponseRedirect(reverse('accounts:create-profile'))
            else:
                return HttpResponseRedirect(reverse('home'))
                
            if not user.profile.id == None:
                auth_login(request, user)
                return HttpResponseRedirect(reverse('home'))
            else:
                auth_login(request, user)
                return HttpResponseRedirect(reverse('accounts:create-profile'))
    return render(request, 'login.html')

@login_required
@csrf_exempt
def dashboard(request):
    if request.method=="POST":
        user_id = request.POST.get('userid')
        
        seat_requests = SeatRequest.objects.filter(request_from__id=user_id, request_to__id=request.user.id)
        print(seat_requests.count())
        for seat_request in seat_requests:
            seat_request.approved = True
            seat_request.save()

    user = request.user
    mentor = user.profile.all()[0].mentor
    if mentor:
        mentoring_list = []
        if user.profile.all()[0].mentor:
            mentor_requests = Mentoring.objects.filter(mentor=user,status=0)
            
            for mentor_request in mentor_requests:
                mentoring_list.append(model_to_dict(mentor_request.startup))
    
    seats = SeatRequest.objects.all().filter(request_to=request.user, approved=False)

    senders = []
    for seat in seats:
        senders.append(model_to_dict(seat.request_from))
    user_dict = model_to_dict(user)
    if not request.user.is_authenticated:
        status = -1
        #context["status"] = -1
    else:    
        #context["status"] = reminder(self.request.user.pk)
        status = reminder(request.user.pk)
        print(status)
    return render(request, 'dashboard.html', {'user':user_dict, 'senders':senders,'status':status})
    

@login_required
def get_coffee(request):
    if Coffee.objects.filter(user=request.user).count() == 0:
        coffee = Coffee(user=request.user)
        coffee.save()
    else:
        coffee =  Coffee.objects.get(user=request.user)
    coffee_log = CoffeeLog()
    time = datetime.today()
    datestring = str(time)
    coffee.total_coffee = coffee.total_coffee + 1 
    coffee.save()
    token = str(request.user.username)+ datestring[:10]  + str(coffee.total_coffee)
    coffee_log.token = token
    coffee_log.user = request.user
    
    if coffee.total_coffee < coffee.free_coffee:
        free_coffee = True
        coffee_left = coffee.free_coffee - coffee.total_coffee
    else:
        free_coffee = False
        coffee_extra = coffee.total_coffee - coffee.free_coffee
        coffee.amount_due = coffee_extra*15
        coffee.save()
        coffee_left = 0
    
    coffee_log.save()
    wallet = request.user.wallet
    amount_due = wallet.coffee_total
    return render(request,'getcoffee.html',context={'token':coffee_log.token,'free':free_coffee,'left':coffee_left,'amount_due':amount_due})

@csrf_exempt
@login_required
def verify_coffee(request):
    if request.method == "POST":
        token = request.POST.get('token')
        if CoffeeLog.objects.filter(token=token).count()==0:
            return render(request,'verify_coffee.html',context={'token':False,'sent':2})
        return render(request,'verify_coffee.html',context={'token':True,'sent':2})
    else:
        return render(request,'verify_coffee.html',context={'token':True,'sent':1})

@csrf_exempt
@login_required
def confirm_mentor(request, pk):

    startup = Startup.objects.get(pk=pk)
    user = request.user

    mentor_requests = Mentoring.objects.filter(startup=startup, mentor=user)
    
    for mentor_request in mentor_requests:
        
        mentor_request.status = 1
        mentor_request.action = user.pk
        mentor_request.save()
    return HttpResponseRedirect(reverse('accounts:dashboard')) 


def reminder(pk):
    user = User.objects.get(id=pk)
    status=0
    print(user.wallet.balance)
    if user.wallet.balance<100:
        status=1
    return status
