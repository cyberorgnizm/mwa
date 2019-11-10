from django.urls import path
from django.views.generic import TemplateView
from profiles.views import SignUpView, StaffSignUpView

app_name="profiles"
urlpatterns = [
    path('profile/', TemplateView.as_view(template_name="profiles/user.html"), name="profile"),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('staff/signup/', StaffSignUpView.as_view(), name='staff-signup'),
]