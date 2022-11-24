from rest_framework import serializers
from .models import Plan, PlanInterests


class PlanSerializer(serializers.ModelSerializer):
    # when = serializers.DateTimeField(source="when").
    class Meta:
        model = Plan
        fields = '__all__'

    # def to_representation(self, obj):
    #     r = super().to_representation(obj)
    #     r['when']

class PlanInterestSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanInterests
        fields = ('interest', 'weight')