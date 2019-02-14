from django.shortcuts import render, reverse
from django.contrib.auth.models import User
from django.views.generic import CreateView
from .forms import UserForm
from django.urls import reverse_lazy
from .models import Profile
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate
from django.core import serializers
from django.forms.models import model_to_dict

class SignUp(CreateView):
    model = User
    form_class = UserForm
    template_name = 'signup.html'
    success_url = reverse_lazy('accounts:login')

    def form_valid(self, form):
        user = form.save(commit = False)
        user.is_active = 0
        super().form_valid(self, form)

class Profile(CreateView):
    model = Profile
    template_name = 'profile.html'
    success_url = reverse_lazy('accounts:profile')

def logout(request):
    auth_logout(request)
    return HttpResponseRedirect(reverse('accounts:login'))

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                auth_login(request, user)
                return HttpResponseRedirect(reverse('accounts:dashboard'))
            else:
                return HttpResponseRedirect(reverse('accounts:create-profile'))
    return render(request, 'login.html')

@login_required
def dashboard(request):
    user = request.user
    user_dict = model_to_dict(user)
    return render(request, 'dashboard.html', {'user':user_dict})