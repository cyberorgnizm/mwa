from django.urls import path
from django.views.generic import TemplateView
from records.views import StatisticsReportView, MedicalReportsView


app_name = "records"
urlpatterns = [
    path("", TemplateView.as_view(template_name="records/dashboard.html"), name="dashboard"),
    path("statistics/", StatisticsReportView.as_view(), name="statistics",),
    path("medical/", MedicalReportsView.as_view(), name="clinic-records",),
]