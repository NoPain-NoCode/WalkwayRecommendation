from django.shortcuts import render
from rest_framework import generics
from rest_framework import mixins
from .models import WalkwayLocation
from .serializers import LocationSerializer

# Create your views here.

class LocationAPI(generics.GenericAPIView, mixins.ListModelMixin):
    serializer_class = LocationSerializer

    def get_queryset(self):  # 어떤 데이터를 가져올 것인지 명시
        return WalkwayLocation.objects.all().order_by('point_number')

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)