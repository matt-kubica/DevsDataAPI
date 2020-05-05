
from rest_framework import views, status, response
from rest_framework.parsers import FileUploadParser

from .models import Event, Registration, Thumbnail
from .serializers import EventSerializer, RegistrationSerializer, ThumbnailSerializer

import uuid
from django.utils import timezone


class EventDetailAPI(views.APIView):

    def get(self, request, pk, format=None):
        try:
            event = Event.objects.get(id=pk)
        except Event.DoesNotExist:
            return response.Response({'error': 'Event {0} id not found.'.format(pk)}, status=status.HTTP_404_NOT_FOUND)

        serializer = EventSerializer(event, many=False)
        return response.Response(serializer.data)


class EventAPI(views.APIView):

    def get(self, request, format=None):
        events = Event.objects.all()
        serializer = EventSerializer(events, many=True)
        return response.Response(serializer.data)

    def post(self, request, format=None):
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ThumbnailAPI(views.APIView):
    parser_classes = (FileUploadParser, )

    def post(self, request, format=None):
        serializer = ThumbnailSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class RegistrationAPI(views.APIView):

    def post(self, request, format=None):
        event_id = request.data['event_id']
        try:
            event = Event.objects.get(id=event_id)
        except Event.DoesNotExist:
            return response.Response({'error': 'There is no event with {0} id.'.format(event_id)}, status=status.HTTP_404_NOT_FOUND)

        data = {
            'event_id': event_id,
            'code': uuid.uuid4()
        }


        serializer = RegistrationSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    @staticmethod
    def is_possible_to_delete(event):
        now = timezone.now().date()
        diff_days = (event.start_date - now).days
        if diff_days < 2:
            return False

        if (event.end_date - event.start_date).days > 2:
            return False

        return True


    def delete(self, request, format=None):
        registration_code = request.data['code']

        try:
            registration = Registration.objects.get(code=registration_code)
        except Registration.DoesNotExist:
            return response.Response({'error': 'There is no registration with {0} code.'.format(registration_code)},
                                     status=status.HTTP_404_NOT_FOUND)

        event = Event.objects.get(id=registration.event_id.id)
        if self.is_possible_to_delete(event):
            registration.delete()
            return response.Response({'info': 'Reservation {0} code cancelled'.format(registration_code)}, status=status.HTTP_200_OK)
        else:
            return response.Response({'error': 'Cancellation is impossible.'}, status=status.HTTP_400_BAD_REQUEST)




