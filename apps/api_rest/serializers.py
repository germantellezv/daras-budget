# DRF
from rest_framework import serializers

# Models
from apps.budget.models import *

class WorkforceSerializer(serializers.HyperlinkedModelSerializer):
    """ Workforce serializer """
    service = serializers.SlugRelatedField(
        slug_field='id',
        many=False,
        read_only=True
    )
    class Meta:
        model = Workforce
        fields = ['id','service','name','experience_time','daily_salary']
