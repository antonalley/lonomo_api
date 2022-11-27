from rest_framework import serializers
from .models import Plan, PlanInterests


def simplify(user):
    return {
        'id': user['id'],
        'username': user['username'],
        'first_name': user['first_name'],
        'last_name': user['last_name'],
        'email': user['email']
    }

class PlanSerializer(serializers.ModelSerializer):
    # when = serializers.DateTimeField(source="when").
    # TODO right now it sends the passwords out because of the depth (though encrypted)
    class Meta:
        model = Plan
        fields = '__all__'
        depth=2

    def to_representation(self, obj):
        r = super().to_representation(obj)
        r['host'] = simplify(r['host'])
        r['people_going'] = [simplify(a) for a in r['people_going']]
        return r

class PlanInterestSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanInterests
        fields = ('interest', 'weight')