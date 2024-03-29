# Generated by Django 2.2.7 on 2019-11-12 17:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0002_auto_20191110_1956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clinicalrecord',
            name='patient',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='patient_record', to='profiles.Patient'),
        ),
        migrations.AlterField(
            model_name='locationrecord',
            name='patient',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='patient_location', to='profiles.Patient'),
        ),
    ]
