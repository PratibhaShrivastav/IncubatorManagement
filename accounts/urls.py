from django.contrib import admin
from django.urls import path
from .views import SignUp, login, logout, dashboard, CreateProfile,get_coffee
from django.contrib.auth import views as auth_views
from django import views

app_name = 'accounts'

urlpatterns = [
    path('signup/',SignUp.as_view(),name='signup'),
    path('login/',login ,name='login'),
    path('logout/',logout ,name='logout'),
    path('dashboard/',dashboard, name='dashboard'),
    path('profile/', CreateProfile.as_view(), name='create-profile'),
    path('coffee/',get_coffee,name='coffee'),
]