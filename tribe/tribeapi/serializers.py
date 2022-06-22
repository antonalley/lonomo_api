from rest_framework import serializers

from .models import Hobby, Person, PersonHobby


class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = ('id', 'firstName', 'lastName', 'school', 'major', 'religion')

class HobbySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hobby
        fields = ('id', 'name',)

class PersonHobbySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PersonHobby
        fields = ('id', 'person','hobby')
