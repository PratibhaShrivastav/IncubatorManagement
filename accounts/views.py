from django.shortcuts import render
from .forms import CreateUserForm
from django.views.generic import CreateView
from django.urls import reverse_lazy

class SignUp(CreateView):
    form_class = CreateUserForm
    template_name = 'signup.html'
    success_url = reverse_lazy('accounts:login')