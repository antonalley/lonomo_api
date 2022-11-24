from django.db import models

from users.models import Interest
from django.contrib.auth.models import User
# Create your models here.

class Plan(models.Model):
    name = models.CharField(max_length=100)
    when = models.DateTimeField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    location_name = models.CharField(max_length=100)
    num_people = models.IntegerField()
    host = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name="host")
    people_going = models.ManyToManyField(User, blank=True, related_name="people_going")
    # interests are a seperate model


class PlanInterests(models.Model):
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    interest = models.ForeignKey(Interest, on_delete=models.CASCADE)
    weight = models.PositiveIntegerField() # 1-10




