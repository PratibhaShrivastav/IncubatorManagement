from django.urls import path,include
from .views import CreateContact

app_name = "contact"

urlpatterns = [
    path('', CreateContact.as_view(), name="send-message")
]

