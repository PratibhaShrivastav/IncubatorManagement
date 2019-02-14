from django.shortcuts import render
from .forms import UserForm
from django.views.generic import CreateView
from .forms import UserForm
from django.urls import reverse_lazy
from .models import Profile
from django.contrib.auth.models import User


class SignUp(CreateView):
    model = User
    form_class = UserForm
    template_name = 'signup.html'
    success_url = reverse_lazy('accounts:login')

    # def form_valid(self, form):
    #     user = form.save(commit = False)
    #     email = self.request.POST.get('email')
    #     profile = Profile()
    #     if Profile.objects.get(user_email=email).exists():
    #         print("Blah")
    #     profile.user_email = email
    #     profile.startup = NULL
    #     profile.user = user
    #     profile.save()
        
    #     super().form_valid(self, form)
