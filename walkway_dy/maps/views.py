from django.shortcuts import render
from rest_framework import generics, mixins
from .serializers import WalkwaySerializer
from .models import WalkwayLocation

# Create your views here.
class WalkwayAPI(generics.GenericAPIView, mixins.ListModelMixin):
    serializer_class = WalkwaySerializer

    def get_queryset(self):
        return WalkwayLocation.objects.all().order_by('point_number')

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
