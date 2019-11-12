from django.urls import path, include
from rest_framework import routers
from api.views import ClinicalRecordsViewSet, PatientViewSet, PractitionerViewSet, UserViewSet


router = routers.DefaultRouter()
router.register("records/clinics", ClinicalRecordsViewSet)
router.register("records/patients", PatientViewSet)
router.register("records/practitioners", PractitionerViewSet)
router.register("records/users", UserViewSet)

urlpatterns = [
    path("", include(router.urls))
]
