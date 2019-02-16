from django import views
from django.views.generic import TemplateView
from accounts.models import Profile

class Home(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profiles = Profile.objects.all()
        profile_list = []
        for profile in profiles:
            if profile.mentor == True:
                profile_list.append(profile)
        context["profiles"] = profile_list
        return context
    