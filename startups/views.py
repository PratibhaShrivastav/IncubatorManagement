from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import StartupLog
from django.urls import reverse_lazy
# Create your views here.

class Startup_Log(CreateView):
    model = StartupLog
    fields = ('update_title','update_description','photo')
    template_name = 'startup_update.html'
    success_url = reverse_lazy('')

    def form_valid(self,form):
        log = form.save(commit=False)
        log.startup = self.request.user.profile.startup
        log.save()
        return super.form_valid(form)

