from django import views
from django.views.generic import TemplateView
from accounts.models import Profile
from accounts.views import reminder

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
        if not self.request.user.is_authenticated:
            context["status"] = -1
        else:    
            context["status"] = reminder(self.request.user.pk)
        print(context["status"])
        return context
    