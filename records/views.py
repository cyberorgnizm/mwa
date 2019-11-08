# from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import permission_required
from profiles.models import Patient


class StatisticsReportView(LoginRequiredMixin, DetailView):
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
    # permission_required = ('custom_user.can_view',)
    template_name = "records/patient_list.html"
