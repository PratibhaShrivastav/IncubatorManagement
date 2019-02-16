from django.shortcuts import render
from .models import ContactUs
from django.views.generic import CreateView
from django.urls import reverse_lazy

class CreateContact(CreateView):
    model = ContactUs
    fields = ('name','email','message')
    template_name = 'contact.html'
    success_url = reverse_lazy('home')
