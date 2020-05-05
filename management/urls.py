from django.urls import path
from .api  import RegistrationAPI, EventDetailAPI, EventAPI, ThumbnailAPI
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('registration', RegistrationAPI.as_view()),
    path('event/<int:pk>', EventDetailAPI.as_view()),
    path('event', EventAPI.as_view()),
    path('event/thumbnail', ThumbnailAPI.as_view())
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)