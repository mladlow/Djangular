from rest_framework import generics, permissions
from .models import Household, DogOwner
from .serializers import HouseholdSerializer, DogOwnerSerializer
from django.shortcuts import render

class HouseholdList(generics.ListCreateAPIView):
    model = Household
    serializer_class = HouseholdSerializer
    permission_classes = [permissions.AllowAny]

class HouseholdDetail(generics.RetrieveAPIView):
    model = Household
    serializer_class = HouseholdSerializer
    lookup_url_kwarg = 'household_pk'
    permission_classes = [permissions.AllowAny]

class DogOwnerUpdate(generics.UpdateAPIView):
    model = DogOwner
    serializer_class = DogOwnerSerializer
    lookup_url_kwarg = 'dogowner_pk'
    permission_classes = [permissions.AllowAny]

class DogOwnerList(generics.ListCreateAPIView):
    model = DogOwner
    serializer_class = DogOwnerSerializer
    permission_classes = [permissions.AllowAny]

def index(request):
    return render(request, 'dogdate/index.html')
