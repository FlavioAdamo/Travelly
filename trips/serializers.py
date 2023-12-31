from rest_framework import serializers
from .models import Trip, Destination
from hotels.serializers import BookingSerializer
from cities.serializers import CitySerializer


class DestinationReadSerializer(serializers.ModelSerializer):
    city = CitySerializer()
    class Meta:
        model = Destination
        fields = ['trip', 'city', 'arrival_date', 'departure_date']


class DestinationWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Destination
        fields = ['trip', 'city', 'arrival_date', 'departure_date']


class TripWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        exclude = ['user']


class TripReadSerializer(serializers.ModelSerializer):
    destinations = DestinationReadSerializer(source='destination_set', many=True)  
    user_name = serializers.CharField(source='user')

    class Meta:
        model = Trip
        fields = ['title', 'user', 'participants', 'start_date', 'end_date', 'budget', 'destinations', 'user_name']


        def to_representation(self, instance):
            rep = super(TripReadSerializer, self).to_representation(instance)
            rep['username'] = instance.user.username
            return rep