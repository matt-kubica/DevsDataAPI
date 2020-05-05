from django.urls import path
from .api  import RegistrationAPI

urlpatterns = [
    path('registration', RegistrationAPI.as_view()),

]