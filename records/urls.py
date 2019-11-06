from django.urls import path
from records.views import StatisticsReportView, MedicalReportsView

urlpatterns = [
    path("statistics/", StatisticsReportView.as_view(), name="statistics",),
    path("medical/", MedicalReportsView.as_view(), name="records",),
]