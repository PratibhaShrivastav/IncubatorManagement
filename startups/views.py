from django.shortcuts import render
from django.views.generic import CreateView,DetailView,ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import StartupLog, Startup
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from aylienapiclient import textapi
import json
from django.forms.models import model_to_dict


class CreateStartup(CreateView):
    model = Startup
    fields = ('name','motto','logo','worth')
    template_name = 'startup_add.html'
    success_url = reverse_lazy('startups:verify-success')


def startup_success(request):
    return render(request, 'submit_startup.html')


class Startup_detail(DetailView):
    model = Startup
    template_name = 'startup_detail.html'
    context_object_name = 'startup'


@csrf_exempt
def check_status(request):
    if request.method == "POST":
        name = request.POST.get('startup_name')
        try:
            startup = Startup.objects.get(name=name)
            status = startup.status
        except:
            status = 4
        
        if status == 0:
            message = "PENDING"
        elif status == 1:
            message = "ACCEPTED"
        elif status == 2:
            message = "REJECTED"
        else:
            message = "ERROR"
        return render(request, "apply_status.html", context={'status':message,'status_code':status})     
    return render(request, "status_form.html")

class StartupList(ListView):
    model = Startup
    template_name = 'startup_list.html'
    context_object_name = 'startup'


@csrf_exempt
@login_required
def submit_log(request):
    if request.method == "POST":
        title = request.POST.get('update_title')
        description = request.POST.get('update_description')
        startup_name = request.POST.get('startup_name')
        startup = Startup.objects.get(name=startup_name)

        #Analyzing Sentiment
        client = textapi.Client("43b31dcf","6d8afe9d7492c69237ee810f368e1c13")
        sentiment_reply = client.Sentiment(description)
        emotion = sentiment_reply['polarity']
        
        if emotion == "neutral":
            sentiment = 0
        elif emotion == "positive":
            sentiment = 1
        else:
            sentiment = -1

        #Creating Log
        log = StartupLog(startup=startup, update_title=title, update_description=description, sentiment=sentiment)
        log.save()
        log = model_to_dict(log)
        return render(request, "log_details.html", context={'log':log})

    return render(request, "create_log.html")