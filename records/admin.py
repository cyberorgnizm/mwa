from django.contrib import admin
from records.models import BloodRecord, MeasurementRecord, LocationRecord, ClinicalRecord


class BloodGroupInline(admin.TabularInline):
    model = BloodRecord


class MeasurementInline(admin.TabularInline):
    model = MeasurementRecord


class LocationRecordInline(admin.TabularInline):
    model = LocationRecord
    

class ClinicalRecordInline(admin.TabularInline):
    model = ClinicalRecord
