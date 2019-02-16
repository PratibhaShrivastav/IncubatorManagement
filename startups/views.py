from django.shortcuts import render
from django.views.generic import CreateView,DetailView,ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import StartupLog, Startup
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt


class CreateStartup(CreateView):
    model = Startup
    fields = ('name','motto','logo','worth')
    template_name = 'startup_add.html'
    success_url = reverse_lazy('startups:verify-success')


class Startup_Log(LoginRequiredMixin, CreateView):
    model = StartupLog
    fields = ('update_title','update_description','photo')
    template_name = 'startup_update.html'
    success_url = reverse_lazy('')

    def form_valid(self, form):
        log = form.save(commit=False)
        log.startup = self.request.user.profile.startup
        log.save()
        return super.form_valid(form)

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
