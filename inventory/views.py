from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import InventorySerializer
from .models import Inventory



# Create your views here.
class InventoryViewSet(viewsets.ModelViewSet):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
    permission_classes = [permissions.AllowAny]
    