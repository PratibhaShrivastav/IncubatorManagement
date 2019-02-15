from django.shortcuts import render, reverse
from django.contrib.auth.models import User
from django.views.generic import CreateView
from .forms import UserForm
from django.urls import reverse_lazy
from .models import Profile as Profile
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate
from django.core import serializers
from django.forms.models import model_to_dict
from django.views.decorators.csrf import csrf_exempt


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
