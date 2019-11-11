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
    User = get_user_model()
    # extra context data for template cards
    users_count = User.objects.all().count()
    patients_count = Patient.objects.all().count()
    practitioners_count = Practitioner.objects.all().count()
    medical_records_count = ClinicalRecord.objects.count()
    
    # used to populate table in template
    medical_records = ClinicalRecord.objects.all()
    
    
    queryset = Patient.objects.all()
    context_object_name = "patients_list"
    template_name = "records/patient_statistics.html"
    extra_context = {
        "users_count": users_count,
        "patients_count": (patients_count / users_count) * 100,
        "practitioners_count": (practitioners_count / users_count) * 100,
        "medical_records_count": medical_records_count,
        
        # table data
        "ebola": medical_records.filter(illness__startswith="Ebola").count,
        "ebola_percentage": round((medical_records.filter(illness__startswith="Ebola").count()/medical_records.count()) *100),
        "malaria": medical_records.filter(illness__startswith="Malaria").count,
        "malaria_percentage": round((medical_records.filter(illness__startswith="Malaria").count()/medical_records.count()) * 100),
        "typhoid": medical_records.filter(illness__startswith="Typhoid").count,
        "typhoid_percentage": round((medical_records.filter(illness__startswith="Typhoid").count()/medical_records.count()) * 100),
        "tuberculosis": medical_records.filter(illness__startswith="Tuberculosis").count,
        "tuberculosis_percentage": round((medical_records.filter(illness__startswith="Tuberculosis").count()/medical_records.count()) * 100),
        "hepatitis": medical_records.filter(illness__startswith="Hepatitis").count,
        "hepatitis_percentage": round((medical_records.filter(illness__startswith="Hepatitis").count()/medical_records.count()) * 100),
        "others": medical_records.filter(illness__startswith="Others").count,
        "others_percentage": round((medical_records.filter(illness__startswith="Others").count()/medical_records.count()) * 100)
    }



class MedicalReportsView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    """
    Displays all users and their relevant medical records
    Permission: (only users registered as medical practitioners can view this page)
    """
    model = Patient
    context_object_name = "patients_list"
    permission_required = ('profiles.view_patient',)
    template_name = "records/patient_list.html"
    