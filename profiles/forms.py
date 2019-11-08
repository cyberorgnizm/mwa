from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from profiles.models import CustomUser, Practitioner
from django.contrib.auth.validators import UnicodeUsernameValidator

"""
The forms below are customized for use with the CustomUser Model in Admin app
"""

class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        # An inner class that provides metadata to ModelForm class
        model = CustomUser
        # fields = '__all__'
        fields = ('first_name', 'middle_name', 'last_name', 'username', 'gender',)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = '__all__'
        


class StaffCreationForm(forms.ModelForm):
    username_validator = UnicodeUsernameValidator()
    field_order = ['title', 'first_name', 'last_name', 'username', 'password']
    
    # custom fields for creating regular user
    username = forms.CharField(validators=[username_validator,])
    password = forms.CharField(max_length=128, widget=forms.PasswordInput)
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    class Meta:
        model = Practitioner
        fields = "__all__"
        exclude = ('profile', 'phone',)
