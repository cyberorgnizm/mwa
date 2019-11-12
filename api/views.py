# from django.shortcuts import render
from rest_framework import viewsets
from records.models import ClinicalRecord
from api.serializers import ClinicalRecordSerializer


class ClinicalRecordsViewSet(viewsets.ModelViewSet):
    queryset = ClinicalRecord.objects.all()
    serializer_class = ClinicalRecordSerializer
