# from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from profiles.forms import CustomUserCreationForm

class SignUpView(CreateView):
    """Generic class that implements form rendering and model creation, used for user registration"""
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = "signup.html"


class StaffSignUpView(CreateView):
    """Staff Creation View used to register new staff"""
    pass
