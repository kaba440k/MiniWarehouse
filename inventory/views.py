from django.shortcuts import render
from rest_framework import generics

from .models import Inventory
from .serializers import InventorySerializer


class InventoryList(generics.ListCreateAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer


class InventoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
# Create your views here.
