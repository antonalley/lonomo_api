from rest_framework import serializers

from .models import Hobby, Person


class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = ('id', 'firstName', 'lastName', 'school', 'major', 'religion')


class HobbySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hobby
        fields = ('id', 'pid', 'name',)
