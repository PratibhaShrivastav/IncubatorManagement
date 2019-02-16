from django.contrib import admin
from django.urls import path
from .views import get_wallet
from django.contrib.auth import views as auth_views

app_name = 'Wallet'

urlpatterns = [
    path('get_wallet/', get_wallet ,name='get_wallet'),
]