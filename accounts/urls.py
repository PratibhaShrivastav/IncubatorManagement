from django.contrib import admin
from django.urls import path
from .views import SignUp, login, logout, dashboard, CreateProfile,get_coffee, verify_coffee, confirm_mentor
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
    path('verify/',verify_coffee, name='verify'),
    path('approve/',dashboard, name='approve_request'),
    path('confirm-mentor/<int:pk>/', confirm_mentor, name='confirm-mentor'),
]