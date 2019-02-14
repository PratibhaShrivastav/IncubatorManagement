from django.contrib import admin
from django.urls import path
from .views import SignUp
from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns = [
    path('signup/',SignUp.as_view(),name='signup'),
    path('login/',auth_views.LoginView.as_view(template_name='login.html'),name='login'),
]