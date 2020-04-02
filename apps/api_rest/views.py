# DRF
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import generics

# Decorators
from rest_framework.decorators import action

# Serializers
from .serializers import *

# Models
from apps.budget.models import *

class MaterialViewSet(viewsets.ModelViewSet):
    """
    API endpoint that lists all materials
    """

    queryset = Material.objects.all()
    serializer_class = MaterialSerializer
    permission_classes = [permissions.IsAuthenticated]

class UnitViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users choose units
    """
    
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer
    permission_classes = [permissions.IsAuthenticated]


class WorkforceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users choose workforces
    """
    queryset = Workforce.objects.all()
    serializer_class = WorkforceSerializer
    permission_classes = [permissions.IsAuthenticated]

class TransportViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users choose Transports
    """
    queryset = Transport.objects.all()
    serializer_class = TransportSerializer
    permission_classes = [permissions.IsAuthenticated]

class SecureViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users choose Secures
    """
    queryset = Secure.objects.all()
    serializer_class = SecureSerializer
    permission_classes = [permissions.IsAuthenticated]

class WorkforceList(generics.ListAPIView):
    """ 
    API endpoint that allows filter workforce by service id
    """

    serializer_class = WorkforceSerializer

    def get_queryset(self):
        """
        This view should return a list of all the worforces
        with specif service id
        """
        service = self.kwargs['service']
        result = Workforce.objects.filter(service=service)
        return result

class MaterialList(generics.ListAPIView):
    """ 
    API endpoint that allows filter materials by service id
    """

    serializer_class = MaterialSerializer

    def get_queryset(self):
        """
        This view should return a list of all the worforces
        with specif service id
        """
        service = self.kwargs['service']
        result = Material.objects.filter(service=service)
        return result

class EquipmentList(generics.ListAPIView):
    """ 
    API endpoint that allows filter workforce by service id
    """

    serializer_class = EquipmentSerializer

    def get_queryset(self):
        """
        This view should return a list of all the worforces
        with specif service id
        """
        service = self.kwargs['service']
        result = Equipment.objects.filter(service=service)
        return result