
# from rest_framework import views, status, response
#
# from .models import Event, Registration
# from .serializers import EventSerializer, RegistrationSerializer
# import uuid
#
#
# class EventDetailAPI(views.APIView):
#     # TODO: permissions???
#
#     def get(self, request, pk, format=None):
#         event = Event.objects.get(id=pk)
#         serializer = EventSerializer(event, many=False)
#         return response.Response(serializer.data)
#
#     # TODO: post
#
#
#
# class RegistrationAPI(views.APIView):
#
#     def
#
#     # def get(self, request, pk, format=None):
#     #     event = Event.objects.get(id=pk)
#     #     data = {
#     #         'event_id': event.id,
#     #         'code': uuid.uuid4()
#     #     }
#     #     serializer = RegistrationSerializer(data=data)
#     #     if serializer.is_valid():
#     #         serializer.save()
#     #         return response.Response(serializer.data, status=status.HTTP_201_CREATED)
#     #     return response.Response(serializer.errors, status=status.HTTP_404_NOT_FOUND) # TODO: or bad request??
#
#
#     def delete(self, request, pk, format=None):
#
#
#
#
