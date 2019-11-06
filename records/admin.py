from django.contrib import admin
from records.models import BloodRecord, MeasurementRecord


class BloodGroupInline(admin.TabularInline):
    model = BloodRecord


class MeasurementInline(admin.TabularInline):
    model = MeasurementRecord
