# from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import permission_required
from django.contrib.auth import get_user_model
from profiles.models import Patient, Practitioner
from records.models import ClinicalRecord



class DashBoardView(LoginRequiredMixin, TemplateView):
    User = get_user_model()
    # extra context data for template cards
    users_count = User.objects.all().count()
    patients_count = Patient.objects.all().count()
    practitioners_count = Practitioner.objects.all().count()
    
    # clinical data
    ebola_count = ClinicalRecord.objects.filter(illness__startswith="Ebola").count()
    malaria_count = ClinicalRecord.objects.filter(illness__startswith="Malaria").count()
    typhoid_count = ClinicalRecord.objects.filter(illness__startswith="Typhoid").count()
    tuberculosis_count = ClinicalRecord.objects.filter(illness__startswith="Tuberculosis").count()
    hepatitis_count = ClinicalRecord.objects.filter(illness__startswith="Hepatitis").count()
    others_count = ClinicalRecord.objects.filter(illness__startswith="Others").count()
    
    extra_context = {
        "users_count": users_count,
        "patients_count": patients_count,
        "practitioners_count": practitioners_count,
        
        # clinical data context
        "ebola_count": ebola_count,
        "malaria_count": malaria_count,
        "typhoid_count": typhoid_count,
        "tuberculosis_count": tuberculosis_count,
        "hepatitis_count": hepatitis_count,
        "others_count": others_count, 
    }
    template_name = "records/dashboard.html"


class StatisticsReportView(LoginRequiredMixin, ListView):
    """
    Statistical details of the medical records gotten from the users
    Permission: (all users can view this page)
    """
    queryset = Patient.objects.all()
    context_object_name = "patients_list"
    template_name = "records/patient_statistics.html"



class MedicalReportsView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    """
    Displays all users and their relevant medical records
    Permission: (only users registered as medical practitioners can view this page)
    """
    model = Patient
    context_object_name = "patients_list"
    permission_required = ('profiles.view_patient',)
    template_name = "records/patient_list.html"
    