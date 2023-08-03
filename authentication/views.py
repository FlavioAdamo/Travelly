from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import UserRegisterSerializer, CustomTokenObtainPairSerializer
from rest_framework.response import Response
from rest_framework import generics


class UserRegisterView(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=400)
        
        user = serializer.save()
        if user: return Response(serializer.data, status=201)


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


