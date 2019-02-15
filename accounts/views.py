from django.shortcuts import render, reverse
from django.contrib.auth.models import User
from django.views.generic import CreateView
from .forms import UserForm
from django.urls import reverse_lazy
from .models import Profile as Profile,Coffee,CoffeeLog,Startup
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate
from django.core import serializers
from django.forms.models import model_to_dict
from django.views.decorators.csrf import csrf_exempt
from datetime import date
import datetime
import base64


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
def dashboard(request):
    user = request.user
    user_dict = model_to_dict(user)
    return render(request, 'dashboard.html', {'user':user_dict})

@login_required
def get_coffee(request):
    if Coffee.objects.filter(user=request.user).count() == 0:
        coffee = Coffee(user=request.user)
        coffee.save()
    else:
        coffee =  Coffee.objects.get(user=request.user)
    coffee_log = CoffeeLog()
    time = datetime.datetime.now()
    datestring = str(time)
    coffee.total_coffee = coffee.total_coffee + 1 
    coffee.save()
    token = str(request.user.username)+datestring
    token = encode('COFFEE', token)
    coffee_log.token = token
    coffee_log.user = request.user
    
    print("free = ",coffee.free_coffee, " | total :",coffee.total_coffee)
    if coffee.total_coffee < coffee.free_coffee:
        free_coffee = True
        coffee_left = coffee.free_coffee - coffee.total_coffee
        amount_due = 0
    else:
        free_coffee = False
        coffee_extra = coffee.total_coffee - coffee.free_coffee
        coffee.amount_due = coffee_extra*15
        amount_due = coffee.amount_due
        coffee.save()
        coffee_left = 0
    
    coffee_log.save()
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


def encode(key, clear):
    enc = []
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

def decode(key, enc):
    dec = []
    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)