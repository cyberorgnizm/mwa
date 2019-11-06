from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    """
    Generic User: 'Implementing a fulling featured user model with admin complaint permissions'
    fields: [
        firs_tname, 
        last_name,
        middle_name(optional),
        gender,
        date_of_birth,
        username, 
        email,
        phone, 
        password,
    ]
    """
    # Limits choice selection in Django forms
    GENDER_SELECT_OPTION = [('M', "Male",), ('F', "Female",)]

    middle_name = models.CharField(max_length=255, blank=True, null=True)
    gender = models.CharField(max_length=1, choices=GENDER_SELECT_OPTION)
    date_of_birth = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.middle_name or ''} {self.last_name}"

    class Meta:
        verbose_name_plural = "Accounts"
    
