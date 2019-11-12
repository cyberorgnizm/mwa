from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from profiles.models import CustomUser, Practitioner
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.validators import EmailValidator


username_validator = UnicodeUsernameValidator()


"""
The forms below are customized for use with the CustomUser Model in Admin app
"""

class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        # An inner class that provides metadata to ModelForm class
        model = CustomUser
        # fields = '__all__'
        fields = ('first_name', 'middle_name', 'last_name', 'username', 'gender',)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = '__all__'
        


class StaffCreationForm(forms.ModelForm):
    field_order = ['title', 'first_name', 'last_name', 'username', 'password']
    
    # custom fields for creating regular user
    username = forms.CharField(validators=[username_validator,])
    password = forms.CharField(max_length=128, widget=forms.PasswordInput)
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    class Meta:
        model = Practitioner
        fields = "__all__"
        exclude = ('profile', 'phone',)


class ProfileForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    middle_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    username = forms.CharField(validators=[username_validator,])
    email = forms.EmailField(validators=[EmailValidator])
    gender = forms.ChoiceField()
    birth_day = forms.DateField()
    blood_group = forms.ChoiceField(
        choices=(
            ("O+", "O(+) Positive",),
            ("O-", "O(-) Negative",),
            ("A+", "A(+) Positive",),
            ("A-", "O(-) Negative",),
            ("AB+", "AB(+) Positive",),
            ("AB-", "AB(-) Negative",)
        ),
    )
    blood_genotype = forms.ChoiceField(
        choices=(
            ("AA", 'AA',),
            ("AO", 'AO',),
            ("AB", 'AB',),
            ("BO", 'BO',),
            ("BB", 'BB',),
            ("OO", 'OO',),
        ),
    )
    height = forms.DecimalField()
    weight = forms.DecimalField()
    town = forms.ChoiceField(
        choices=(
            ("Abaji", "Abaji",),
            ("Garki", "Garki",),
            ("Bwari", "Bwari",),
            ("Kuje", "Kuje",),
            ("Dutse", "Dutse",),
            ("Gwagwalada", "Gwagwalada",),    
        ),
    )
    clinic_test = forms.ChoiceField(
        choices=(
            ("Ebola", "Ebola",),
            ("Malaria", "Malaria",),
            ("Typhoid", "Typhoid",),
            ("Hepatitis", "Hepatitis",),
            ("Tuberculosis", "Tuberculosis",),
            ("Others", "Others",),
        ),
    )
    test_description = forms.CharField(widget=forms.Textarea)
    test_result = forms.ChoiceField(widget=forms.CheckboxInput)