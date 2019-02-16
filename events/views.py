from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Event
from django.forms.models import model_to_dict


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

def event_all(request):
    events = Event.objects.all()
    event_list = []
    for event in events:
        event_list.append(model_to_dict(event))
    
    context = {'events' : event_list}
    return render(request,'all_event.html', context=context)

def show_event(request, pk):
    event = Event.objects.get(id=pk)
    try:
        startup = event.startup.all()[0]
        startup = model_to_dict(startup)
    except:
        startup = None
    event = model_to_dict(event)
    return render(request, 'show_event.html', context={'event':event,'startup':startup})