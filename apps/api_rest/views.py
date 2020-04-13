# DRF
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import generics
from rest_framework import views
from rest_framework.response import Response
from rest_framework import status


# Decorators
from rest_framework.decorators import action
from rest_framework.decorators import api_view

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
    API endpoint that allows list equipments and tools
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

class CreateBudgetItem(views.APIView):
    """
    API endpoint that allows post Budget item
    """
    def post(self, request, budget_id):
        # Get Budget ID from the URL
        budget = Budget.objects.get(id=budget_id)
        # Get description from a form sent by fetch/ajax in template
        description = request.data.get('description')
        # Get duration from a form sent by fetch/ajax in template
        duration = request.data.get('duration')
        
        data = {'budget':budget.id,'description':description, 'duration':duration}
        serializer = BudgetItemSerializer(data=data)
        if serializer.is_valid():
            # Save instance in database
            item = serializer.save()
            # Return the instance serialized
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Reponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            

class BudgetSubItemList(generics.ListAPIView):
    """ 
    API endpoint that allows filter subitems
    """

    serializer_class = BudgetSubItemSerializer

    def get_queryset(self):
        """
        This view should return a list of all the worforces
        with specif service id
        """
        slug = self.kwargs['budget_slug']
        b = Budget.objects.get(slug=slug)
        slug2 = self.kwargs['item_slug']
        i = BudgetItem.objects.get(slug=slug2)

        result = BudgetSubItem.objects.filter(budget=b, item=i)
        return result

@api_view(['GET','POST'])
def addBudgetSubitem(request, budget_pk, budgetItem_id):
    budget = Budget.objects.get(id=budget_pk)
    item = BudgetItem.objects.get(id=budgetItem_id)

    if request.method == 'POST':
        # Unit instance
        u = Unit.objects.get(id=request.data.get('unit'))

        # Create subitem to after add it to the item
        subitem = BudgetSubItem()
        subitem.budget = budget
        subitem.description = request.data.get('description')
        subitem.unit = u
        subitem.amount = request.data.get('amount')
        subitem.save()

        # Create item and add subitem to item
        item = BudgetItem.objects.get(id=budgetItem_id)
        item.subitems.add(subitem)

        return Response({'id':subitem.id,'description':subitem.description,'unit':subitem.unit.name,'amount':subitem.amount})
    return Response({"message": "Hello, world!","item_id":item.id})