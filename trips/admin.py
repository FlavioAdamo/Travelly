from django.contrib import admin
from .models import (
   Trip,
   Destination
)


admin.site.register(Trip)
admin.site.register(Destination)