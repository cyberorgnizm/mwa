from django.urls import path
from profiles.views import SignUpView


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
]