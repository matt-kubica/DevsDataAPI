
from rest_framework import views, status, response

from .models import Event, Registration
from .serializers import EventSerializer, RegistrationSerializer

import uuid
from django.utils import timezone


class EventDetailAPI(views.APIView):
    # TODO: permissions???

    def get(self, request, pk, format=None):
        event = Event.objects.get(id=pk)
        serializer = EventSerializer(event, many=False)
        return response.Response(serializer.data)

    # TODO: post



class RegistrationAPI(views.APIView):

    def post(self, request, format=None):
        event_id = request.data['event_id']
        if Event.objects.get(id=event_id) is None:
            return response.Response({'error': 'There is no event with {0} id.'.format(id)}, status=status.HTTP_404_NOT_FOUND)

        data = {
            'event_id': id,
            'code': uuid.uuid4()
        }

        serializer = RegistrationSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    @staticmethod
    def is_possible_to_delete(event):
        now = timezone.now()
        diff_days = (event.start_date - now).days
        if diff_days < 2:
            return False

        if (event.end_date - event.start_date).days > 2:
            return False

        return True


    def delete(self, request, format=None):
        registration_code = request.data['code']
        registration = Registration.objects.get(code=registration_code)
        if registration is None:
            return response.Response({'error': 'There is no registration with {0} code.'.format(registration_code)},
                                     status=status.HTTP_404_NOT_FOUND)

        event = Event.objects.get(id=registration.event_id)
        if self.is_possible_to_delete(event):
            registration.delete()




