from django.shortcuts import render
from rest_framework import viewsets
from .serializers import HobbySerializer, PersonSerializer
from .models import Hobby, Person


# Create your views here.

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all().order_by('id')
    serializer_class = PersonSerializer


class HobbyViewSet(viewsets.ModelViewSet):
    queryset = Hobby.objects.all().order_by('pid')
    serializer_class = HobbySerializer


