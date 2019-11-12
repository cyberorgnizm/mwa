# from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth import get_user_model
from records.models import ClinicalRecord
from profiles.models import Patient, Practitioner
from api.serializers import ClinicalRecordSerializer, PatientSerializer, PractitionerSerializer, UserSerializer


class ClinicalRecordsViewSet(viewsets.ModelViewSet):
    queryset = ClinicalRecord.objects.all()
    serializer_class = ClinicalRecordSerializer


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    

class PractitionerViewSet(viewsets.ModelViewSet):
    queryset = Practitioner.objects.all()
    serializer_class = PractitionerSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer