from django.contrib import admin
# from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseAdmin
from profiles.forms import CustomUserChangeForm, CustomUserCreationForm
from profiles.models import CustomUser, Practitioner, Patient
from records.admin import BloodGroupInline, MeasurementInline


@admin.register(CustomUser)
class CustomUserAdmin(BaseAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm

    models = CustomUser
    list_display = ['pk', 'username', 'email', 'first_name', 'last_name', 'date_of_birth', 'gender']



@admin.register(Practitioner)
class PractitionerAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'profile', 'username', 'email', 'phone']



@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    inlines = [
        BloodGroupInline,
        MeasurementInline,
    ]
    list_display = ['id', 'profile', 'email', 'birth_day', 'gender', 'phone', 'address',]