from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, FormView
from profiles.forms import CustomUserCreationForm, StaffCreationForm, ProfileForm, StaffProfileForm
from profiles.models import CustomUser, Practitioner, Patient
# Django permissions
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.db import IntegrityError
from django.http.response import HttpResponseRedirect



class SignUpView(CreateView):
    """Generic class that implements form rendering and model creation, used for user registration"""
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = "profiles/signup.html"
    model = CustomUser
    
    def form_valid(self, form):
        super().form_valid(form)
        try:
            Patient.objects.create(profile=self.object)
        except IntegrityError as e:
            return super().form_invalid(form)
        else:
            
            return HttpResponseRedirect(self.get_success_url())
    
    
    
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
    # form_class = ProfileForm if not self.request.user else StaffProfileForm
    success_url = "/records/"
    
    
    def get_form_class(self):
        form_class = StaffProfileForm if self.request.user.is_staff else ProfileForm
        return form_class
    
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        user = self.request.user
        return ctx
        
    
    def form_valid(self, form):
        user = self.request.user
        if user.is_staff:
            data = form.cleaned_data
            print(data)
            user.first_name = data["first_name"]
            # user.middle_name = data["middle_name"]
            user.last_name = data["last_name"]
            user.email = data["email"]
            user.gender = data["gender"]
            user.date_of_birth = data["date_of_birth"]
            user.save()
            
            # obtains current practitioner with current user as profile
            practitioner = Practitioner.objects.filter(profile=user)[0]
            practitioner.phone = data["phone"]
            practitioner.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            data = form.cleaned_data
            print(data)
            user.first_name = data["first_name"]
            # user.middle_name = data["middle_name"]
            user.last_name = data["last_name"]
            user.email = data["email"]
            user.gender = data["gender"]
            user.date_of_birth = data["birth_day"]
            user.save()
            
            patient = Patient.objects.filter(profile=user)[0]
            # patient.patient_record.illness = data["clinic_test"]
            # patient.patient_record.test_result = data["test_result"]
            # patient.patient_record.description = data["test_description"]
            # patient.patient_location.town = data["town"]
            # patient.patient_measurement.height = data["height"]
            # patient.patient_measurement.weight = data["weight"]
            # patient.patient_blood_record.blood_group = data["blood_group"]
            # patient.patient_blood_record.blood_genotype = data["blood_genotype"]
            patient.save()
            return HttpResponseRedirect(self.get_success_url())