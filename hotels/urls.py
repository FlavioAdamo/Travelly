from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HotelView, BookingView


router = DefaultRouter()
router.register(r'hotels', HotelView)
router.register(r'bookings', BookingView)


urlpatterns = [
   path('', include(router.urls)),
]