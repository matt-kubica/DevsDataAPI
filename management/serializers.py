from rest_framework import serializers
from .models import Event, Registration


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = 'id, title, start_date, end_date' # TODO: thumbnail????


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = '__all__'

