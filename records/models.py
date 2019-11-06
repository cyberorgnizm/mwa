from django.db import models


class BloodRecord(models.Model):
    BLOOD_GROUP_OPTION = (
        ("O+", "O(+) Positive",),
        ("O-", "O(-) Negative",),
        ("A+", "A(+) Positive",),
        ("A-", "O(-) Negative",),
        ("AB+", "AB(+) Positive",),
        ("AB-", "AB(-) Negative",)
    )

    BLOOD_GENOTYPE_OPTION = (
        ("AA", 'AA',),
        ("AO", 'AO',),
        ("AB", 'AB',),
        ("BO", 'BO',),
        ("BB", 'BB',),
        ("OO", 'OO',),
    )

    profile = models.OneToOneField(
        'profiles.Patient', 
        on_delete=models.CASCADE,
    )

    blood_group = models.CharField(max_length=3)
    blood_genotype = models.CharField(max_length=2)



class MeasurementRecord(models.Model):
    profile = models.OneToOneField(
        'profiles.Patient', 
        on_delete=models.CASCADE,
    )

    height = models.DecimalField(verbose_name="height (m/cm)", max_digits=10, decimal_places=2)
    weight = models.DecimalField(verbose_name="weight (kg)", max_digits=10, decimal_places=2)
