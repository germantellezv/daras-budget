# DRF
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import generics


# Serializers
from .serializers import WorkforceSerializer

# Models
from apps.budget.models import Workforce

class WorkforceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users choose workforces
    """
    queryset = Workforce.objects.all()
    serializer_class = WorkforceSerializer
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