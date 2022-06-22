from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView, Response
from .serializers import HobbySerializer, PersonHobbySerializer, PersonSerializer
from .models import Hobby, Person, PersonHobby


# Create your views here.

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all().order_by('id')
    serializer_class = PersonSerializer

class HobbyViewSet(viewsets.ModelViewSet):
    queryset = Hobby.objects.all().order_by('id')
    serializer_class = HobbySerializer

class PersonHobbyViewSet(viewsets.ModelViewSet):
    queryset = PersonHobby.objects.all().order_by('id')
    serializer_class = PersonHobbySerializer

class PersonsHobbiesView(APIView):
    def get(self, request):
        try:
            person = Person.objects.get(id=request.GET.get('pid'))
            hobbies = list(person.hobbies.all().values())
            return Response(hobbies)
        except:
            return Response([])
        
class SimilarHobbies(APIView):
    def get(self, request):
        try:
            similar_hobbies = []
            personal_hobbies = []
            person = Person.objects.get(id=request.GET.get('pid'))
            personal_hobbies_hp = PersonHobby.objects.filter(person=person.id)
            for hp in personal_hobbies_hp:
                personal_hobbies.append(hp.hobby)
                
            all_hobbies = PersonHobby.objects.all()
            for hobby in all_hobbies:
                if hobby.hobby in personal_hobbies:
                    similar_hobbies.append(hobby.person)
            return Response(similar_hobbies)
        except:
            return Response([])

def similarHobbies(request):
    """
        Returns a list of persons that share hobbies wih person
    """
    similar_hobbies = []
    personal_hobbies = []
    person = Person.objects.get(id=request.GET.get('pid'))
    personal_hobbies_hp = PersonHobby.objects.filter(person=person.id)
    for hp in personal_hobbies_hp:
        personal_hobbies.append(hp.hobby)
        
    all_hobbies = PersonHobby.objects.all()
    for hobby in all_hobbies:
        if hobby.hobby in personal_hobbies:
            similar_hobbies.append(hobby.person)

    return JsonResponse(similar_hobbies, safe=False)