from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import CityView


router = DefaultRouter()
router.register(r'cities', CityView)


urlpatterns = [
   path('', include(router.urls)),
]