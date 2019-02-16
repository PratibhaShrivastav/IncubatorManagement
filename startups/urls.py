from django.contrib import admin
from django.urls import path,include
from .views import Startup_Log, CreateStartup, startup_success,Startup_detail, check_status,StartupList

app_name = 'startups'

urlpatterns = [
    path('<int:pk>/create-log/',Startup_Log.as_view(),name='create-log'),
    path('verify-startup/',CreateStartup.as_view(),name='verify-startup'),
    path('verify-startup/success/',startup_success,name='verify-success'),
    path('<int:pk>/',Startup_detail.as_view(),name='startup-detail'),
    path('status/', check_status , name='check_status'),
    path('all/',StartupList.as_view(),name='all-startups'),
]
