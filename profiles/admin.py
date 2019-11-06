from django.contrib import admin
# from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseAdmin
from profiles.forms import CustomUserChangeForm, CustomUserCreationForm
from profiles.models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(BaseAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm

    models = CustomUser
    list_display = ['username', 'email', 'first_name', 'last_name', 'date_of_birth', 'gender']

