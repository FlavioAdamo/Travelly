
from .serializers import HotelSerializer, BookingSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from .models import Hotel, Booking


class HotelView(viewsets.ModelViewSet):
   queryset = Hotel.objects.all()
   serializer_class = HotelSerializer
   permission_classes = [IsAuthenticated]


class BookingView(viewsets.ModelViewSet):
   queryset = Booking.objects.all()
   serializer_class = BookingSerializer
   permission_classes = [IsAuthenticated]

   def perform_create(self, serializer):
      serializer.save(user=self.request.user)