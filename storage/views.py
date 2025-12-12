from django.shortcuts import render
from rest_framework import generics

from .models import Storage
from .serializers import StorageSerializer


class StorageList(generics.ListCreateAPIView):
    queryset = Storage.objects.all()
    serializer_class = StorageSerializer


class StorageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Storage.objects.all()
    serializer_class = StorageSerializer
# Create your views here.
