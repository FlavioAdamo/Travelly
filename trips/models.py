from django.contrib.auth.models import User
from cities.models import City
from django.db import models


class Trip(models.Model):
   title = models.CharField(max_length=200)
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   participants = models.ManyToManyField(User, related_name="participant_trips")
   start_date = models.DateField()
   end_date = models.DateField()
   budget = models.DecimalField(max_digits=10, decimal_places=2)

   def __str__(self):
      return self.title


class Destination(models.Model):
   trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
   city = models.ForeignKey(City, on_delete=models.CASCADE)
   arrival_date = models.DateField()
   departure_date = models.DateField()

   def __str__(self):
      return f'{self.city} - {self.trip}'