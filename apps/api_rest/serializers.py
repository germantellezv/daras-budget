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

class ActivityCategorySerializer(serializers.HyperlinkedModelSerializer):
    service = serializers.SlugRelatedField(
        slug_field='id',
        many=False,
        read_only=True
    )
    class Meta:
        model = ActivityCategory
        fields = ['id','title', 'service','slug']

class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = ['id','acronym', 'name']

class TransportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transport
        fields = ['id', 'name','daily_price']

class SecureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Secure
        fields = ['id', 'name','daily_price']

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id','name', 'budget_type','slug']

class MaterialSerializer(serializers.ModelSerializer):
    service = serializers.SlugRelatedField(
        slug_field='id',
        many=False,
        read_only=True
    )
    unit = serializers.SlugRelatedField(
        slug_field='acronym',
        many=False,
        read_only=True
    )
    class Meta:
        model = Material
        fields = ['id','name', 'unit','service','daily_price','slug','created','modified']

class EquipmentAndToolsSerializer(serializers.ModelSerializer):
    
    service = serializers.SlugRelatedField(
        slug_field='id',
        many=False,
        read_only=True
    )

    class Meta:
        model = Equipment
        fields = ['id','name','service','daily_price']

class EquipmentSerializer(serializers.HyperlinkedModelSerializer):
    """ Equipment serializer """
    service = serializers.SlugRelatedField(
        slug_field='id',
        many=False,
        read_only=True
    )
    class Meta:
        model = Equipment
        fields = ['id','service','name','daily_price','slug','created','modified']

class BudgetItemSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = BudgetItem
        fields = ['id','budget', 'description']

class BudgetSubItemSerializer(serializers.HyperlinkedModelSerializer):
    """ BudgetSubItem serializer """
    budget = serializers.SlugRelatedField(
        slug_field='id',
        many=False,
        read_only=True
    )
    item = serializers.SlugRelatedField(
        slug_field='id',
        many=False,
        read_only=True
    )
    unit = serializers.SlugRelatedField(
        slug_field='id',
        many=False,
        read_only=True
    )
    class Meta:
        model = BudgetSubItem
        fields = ['id','budget','item','description','unit','amount','unit_value','total_value','slug']

