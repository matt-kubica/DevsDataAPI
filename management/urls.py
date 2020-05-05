from django.urls import path
from .api  import RegistrationAPI, EventDetailAPI, EventAPI

urlpatterns = [
    path('registration', RegistrationAPI.as_view()),
    path('event/<int:pk>', EventDetailAPI.as_view()),
    path('events', EventAPI.as_view()),
]