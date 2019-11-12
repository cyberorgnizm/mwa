from django.urls import path, include
from rest_framework import routers
from api.views import ClinicalRecordsViewSet


router = routers.DefaultRouter()
router.register("records", ClinicalRecordsViewSet)

urlpatterns = [
    path("", include(router.urls))
]
