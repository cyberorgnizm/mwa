from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class CustomUser(AbstractUser):
    """
    Generic User: 'Implementing a fulling featured user model with admin complaint permissions'
    fields: [
        first_name, 
        last_name,
        middle_name(optional),
        gender,
        date_of_birth,
        username, 
        email, 
        password,
    ]
    """
    # Limits choice selection in Django forms
    GENDER_SELECT_OPTION = [('M', "Male",), ('F', "Female",),]

    middle_name = models.CharField(max_length=255, blank=True, null=True)
    gender = models.CharField(max_length=1, choices=GENDER_SELECT_OPTION)
    date_of_birth = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.middle_name or ''} {self.last_name}"

    class Meta:
        verbose_name_plural = "Accounts"
    


class Practitioner(models.Model):
    """Practitioner User: This model extends the Generic User for practitioners"""
    TITLE_SELECT_OPTION = [
        ('Dr', "Doctor (Dr)",), 
        ('LPN', 'Licensed practical nurse (LPN)',),
        ('RN', 'Registered nurse (RN)',),
        ('APRN', ' Advanced practice registered nurse (APRN)',),
    ]

    title = models.CharField(max_length=5, verbose_name="title (role)", choices=TITLE_SELECT_OPTION)
    profile = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        verbose_name="profile name", 
        on_delete=models.CASCADE,
    )
    phone = models.CharField(verbose_name="phone number", max_length=20, blank=True, null=True)

    def __str__(self):
        if not self.title.startswith('Dr'):
            return f"{self.profile} {self.title}"
        return f"{self.title} {self.profile}"

    def email(self):
        return self.profile.email

    def username(self):
        return self.profile.username



class Patient(models.Model):
    """Pateint Use: This model extends the Generic User for patients"""
    profile = models.OneToOneField(
        settings.AUTH_USER_MODEL, 
        verbose_name="profile name", 
        on_delete=models.CASCADE
    )
    phone = models.CharField(verbose_name="phone number", max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.profile}"

    def email(self):
        return self.profile.email

    def birth_day(self):
        return self.profile.date_of_birth
    
    def gender(self):
        return self.profile.gender
