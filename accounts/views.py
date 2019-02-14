from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import CreateView
from django.urls import reverse_lazy

class SignUp(CreateView):
    model = User
    fields = ('username','first_name','last_name','password')
    template_name = 'signup.html'
    success_url = reverse_lazy('')