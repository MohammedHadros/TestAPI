from django.shortcuts import render
from rest_framework import viewsets
from .models import Country
from .serializers import CountrySerializer
# Create your views here.
# countries/views.py

class CountryViewSet(viewsets.ModelViewSet):
    serializer_class = CountrySerializer
    queryset = Country.objects.all()