from rest_framework import serializers
from records.models import ClinicalRecord, BloodRecord, LocationRecord
from profiles.models import Patient, Practitioner
from django.contrib.auth import get_user_model


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["username", 'email', 'first_name', 'last_name']

class PatientSerializer(serializers.ModelSerializer):
    profile = UserSerializer()
    class Meta:
        model = Patient
        fields = "__all__"

class ClinicalRecordSerializer(serializers.HyperlinkedModelSerializer):
    patient = PatientSerializer()
    class Meta:
        model = ClinicalRecord
        fields = ['illness', 'test_result', 'patient']