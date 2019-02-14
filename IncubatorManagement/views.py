from django import views
from django.views.generic import TemplateView

class Home(TemplateView):
    template_name = 'home.html'