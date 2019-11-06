from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from profiles.models import CustomUser


"""
The forms below are customized for use with the CustomUser Model in Admin app
"""

class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        # An inner class that provides metadata to ModelForm class
        model = CustomUser
        fields = '__all__'


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = '__all__'