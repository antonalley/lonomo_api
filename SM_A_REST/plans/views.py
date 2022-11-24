from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.views import Response
# from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User

from .models import Plan, PlanInterests
from .serializers import PlanInterestSerializer, PlanSerializer
# Create your views here.

class GetUserPlansView(viewsets.ModelViewSet):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer
    permission_classes = (IsAuthenticated, )

    def list(self, request):
        user = request.user
        is_search = request.GET.get('is_search', 'false')
        if is_search == 'true':
            search_term = request.GET.get('search_term', '')
            self.queryset = self.queryset.filter(name__icontains=search_term)
            print(self.queryset)
        else:
            self.queryset = self.queryset.filter(people_going=user)
        return super().list(request)

    def create(self, request):
        print("Create new plan")
        print(request.data)
        new_plan = Plan.objects.create(
            name=request.data['name'],
            when=request.data['when'],
            latitude=request.data['latitude'],
            longitude=request.data['longitude'],
            location_name=request.data['location_name'],
            num_people=request.data['num_people'],
            host=User.objects.get(id=request.data['host']),
            # people_going=request.data['people_going'],
        )
        for u in User.objects.filter(id__in=request.data['people_going']):
            new_plan.people_going.add(u)
        return Response(status=status.HTTP_201_CREATED) #super().create(request)


class InterestsForPlan(viewsets.ModelViewSet):
    queryset = PlanInterests.objects.all()
    serializer_class = PlanInterestSerializer
    


@api_view(['POST'])
def request_join_event(request):
    plan_id = request.data
    print('Plan id:', plan_id)
    user = request.user
    plan = Plan.objects.get(id=plan_id)
    print("Plan name", plan.name)
    plan.people_going.add(user)
    print('user', user.id)
    return Response(status=status.HTTP_202_ACCEPTED)

@api_view(['POST'])
def leave_event(request):
    print('leave')
    plan_id = request.data
    print('plan id', plan_id)
    user = request.user
    plan = Plan.objects.get(id=plan_id)
    print("Plan name", plan.name)
    print('user', user.id)
    plan.people_going.remove(user)
    return Response(status=status.HTTP_202_ACCEPTED)