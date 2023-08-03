from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from .models import Trip, Destination
from rest_framework import viewsets
from .serializers import (
   DestinationWriteSerializer,
   DestinationReadSerializer,
   TripWriteSerializer,
   TripReadSerializer,
)

# ViewSet for Trip model with CRUD operations
class TripView(viewsets.ModelViewSet):
   queryset = Trip.objects.all()
   permission_classes = [IsAuthenticated]

   # Choose the appropriate serializer class based on the request method
   def get_serializer_class(self):
      if self.request.method in ['GET']:
         return TripReadSerializer
      return TripWriteSerializer

   # Filter the queryset to show only trips belonging to the requesting user
   def get_queryset(self):
      return Trip.objects.filter(user=self.request.user)

   # Assign the current user as the owner when creating a new trip
   def perform_create(self, serializer):
      serializer.save(user=self.request.user)

   # Get an object and check if the requesting user has permission to access it
   def get_object(self):
      obj = super().get_object()
      if obj.user == self.request.user or self.request.user in obj.participants.all():
         return obj
      
      raise PermissionDenied('You do not have permission to access this trip.')


class DestinationView(viewsets.ModelViewSet):
   queryset = Destination.objects.all()
   permission_classes = [IsAuthenticated]

   def get_serializer_class(self):
      if self.request.method in ['GET']:
         return DestinationReadSerializer
      return DestinationWriteSerializer
   
   # Allow creating a new destination only if the requesting user is the trip owner or a participant
   def perform_create(self, serializer):
      trip = Trip.objects.get(id=self.request.data['trip'])
      if self.request.user == trip.user or self.request.user in trip.participants.all():
         serializer.save()
      else:
         raise PermissionDenied('You do not have permission to add a destination to this trip.')