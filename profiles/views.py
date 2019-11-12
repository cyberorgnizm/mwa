from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, FormView
from profiles.forms import CustomUserCreationForm, StaffCreationForm, ProfileForm
from profiles.models import CustomUser, Practitioner, Patient
# Django permissions
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

class SignUpView(CreateView):
    """Generic class that implements form rendering and model creation, used for user registration"""
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = "profiles/signup.html"
    model = Patient
    
    def form_valid(self, form):
        user = CustomUser(
            username=form.cleaned_data["username"],
            first_name=form.cleaned_data["first_name"],
            last_name=form.cleaned_data["last_name"],
        )
        user.set_password(form.cleaned_data["password1"])
        user.save()
        
        form.instance.profile = user
        
        return super().form_valid(form)

class StaffSignUpView(CreateView):
    """A class based view for creating Medical Practitioners"""
    form_class = StaffCreationForm
    success_url = reverse_lazy("login")
    template_name = "profiles/staff/signup.html"
    model = Practitioner
    
    
    def form_valid(self, form):
        user = CustomUser(
            username=form.cleaned_data["username"],
            first_name=form.cleaned_data["first_name"],
            last_name=form.cleaned_data["last_name"],
        )
        user.set_password(form.cleaned_data["password"])
        user.is_staff = True
        user.save()
        # sets permission for practitioner
        content_type = ContentType.objects.get_for_model(Patient)
        permission = Permission.objects.get(
            codename='view_patient',
            content_type=content_type,
        )
        user.user_permissions.add(permission)
        user.save()
        # end permission session
        
        form.instance.title = form.cleaned_data["title"]
        form.instance.profile = user
        
        return super().form_valid(form)


class ProfileView(FormView):
    template_name="profiles/user.html"
    form_class = ProfileForm
    success_url = "/accounts/profile"
    
    