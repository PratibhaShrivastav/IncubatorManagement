from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Event
# Create your views here.

class CreateEvent(LoginRequiredMixin,CreateView):
    model = Event
    fields = ('title','description','start_date','end_date','category','location')
    template_name = 'create_event.html'
    success_url = reverse_lazy('home')

    def form_valid(self,form):
        event = form.save(commit=False)
        event.startup = self.request.user.profile.all()[0].startup
        event.save()
        return super().form_valid(form)
