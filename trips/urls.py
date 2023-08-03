from rest_framework.routers import DefaultRouter
from .views import TripView, DestinationView
from django.urls import path, include

router = DefaultRouter()
router.register(r'trips', TripView)
router.register(r'destinations', DestinationView)

urlpatterns = [
   path('', include(router.urls)),
]