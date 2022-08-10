from django.contrib.auth.models import User
from rest_framework import serializers, validators

from .models import Interest, PersonInterest


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'first_name', 'last_name')

        extra_kwargs = {
            "username": {
                "required": True,
                "allow_blank": False,
                "validators": [
                    validators.UniqueValidator(User.objects.all(), "A user with that username already exists")
                ]
            },
            "first_name": {"required": True, "allow_blank": False},
            "last_name": {"required": True, "allow_blank": False},
            "password": {"required": True, "allow_blank": False, "write_only": True},
            "email": {
                "required": True,
                "allow_blank": False,
                "validators": [
                    validators.UniqueValidator(User.objects.all(), "A user with that Email already exists")
                ]
            }
        }

    def create(self, validated_data):
        username = validated_data.get('username')
        password = validated_data.get('password')
        email = validated_data.get('email')
        first_name = validated_data.get('first_name')
        last_name = validated_data.get('last_name')
        user = User.objects.create(
            username=username,
            password=password,
            email=email,
            first_name=first_name,
            last_name=last_name,
        )

        return user

class InterestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interest
        fields = ("id", "name", "open_response")

class PersonInterestSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonInterest
        fields = ("interest", "person", "detail")
