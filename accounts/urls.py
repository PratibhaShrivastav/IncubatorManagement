from django.contrib import admin
from django.urls import path
from .views import SignUp, login, logout, dashboard
from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns = [
    path('signup/',SignUp.as_view(),name='signup'),
    path('login/',login ,name='login'),
    path('logout/',logout ,name='logout'),
    path('dashboard/',dashboard, name='dashboard'),
]