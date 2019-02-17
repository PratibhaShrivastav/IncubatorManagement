from django.contrib import admin
from django.urls import path,include
from .views import submit_log, CreateStartup, startup_success,Startup_detail, check_status,StartupList, request_mentor

app_name = 'startups'

urlpatterns = [
    path('create-log/',submit_log,name='create_log'),
    path('verify-startup/',CreateStartup.as_view(),name='verify-startup'),
    path('verify-startup/success/',startup_success,name='verify-success'),
    path('<int:pk>/',Startup_detail.as_view(),name='startup-detail'),
    path('status/', check_status , name='check_status'),
    path('all/',StartupList.as_view(),name='all-startups'),
    path('apply-mentor/<int:pk>/',request_mentor, name='apply-mentor'),
]
