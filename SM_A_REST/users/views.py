from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from knox.auth import AuthToken

from .models import Interest, PersonInterest
from .serializers import RegisterSerializer, InterestSerializer, PersonInterestSerializer


@api_view(['POST'])
def login_api(request):
    serializer = AuthTokenSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data['user']

    _, token = AuthToken.objects.create(user)

    return Response({
        'personID': user.id,
        'username': user.username,
        'authtoken': token,
        'success': True,
    })


@api_view(['GET'])
def get_user_data(request):
    user = request.user

    if user.is_authenticated:
        return Response({
            'user_info': {
                'id': user.id,
                'username': user.username,
                'email': user.email
            }
        })

    return Response({
        'error': 'not authenticated'
    }, status=400)


@api_view(['POST'])
def register_api(request):
    serializer = RegisterSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    user = serializer.save()
    _, token = AuthToken.objects.create(user)

    return Response({
        'personID': user.id,
        'username': user.username,
        'authtoken': token,
        'success': True,
    })


class InterestViewSet(viewsets.ModelViewSet):
    queryset = Interest.objects.filter(required=True)
    serializer_class = InterestSerializer

class PersonInterestViewSet(viewsets.ModelViewSet):
    queryset = PersonInterest.objects.all()
    serializer_class = PersonInterestSerializer


