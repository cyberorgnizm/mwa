from django.urls import path
from profiles.views import SignUpView, StaffSignUpView


urlpatterns = [
    # path('staff-signup/', StaffSignUpView.as_view(), name="staff-signup"),
    path('signup/', SignUpView.as_view(), name='signup'),
]