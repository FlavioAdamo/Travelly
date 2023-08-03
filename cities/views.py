from rest_framework.permissions import IsAuthenticated
from .serializers import CitySerializer 
from rest_framework import viewsets
from .models import City


class CityView(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    permission_classes = [IsAuthenticated]
