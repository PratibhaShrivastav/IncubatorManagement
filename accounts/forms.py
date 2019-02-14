from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms

class CreateUserForm(UserCreationForm):
    
    first_name = forms.CharField()
    last_name = forms.CharField()

    class meta:
        fields=('username','first_name','last_name','password1','password2')
        model=get_user_model