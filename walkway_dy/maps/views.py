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

class NearInfoView(View):
    serializer_class = WalkwaySerializer
    
    def get(self, request):
        try:
            longitude = float(request.GET.get('longitude', None))
            latitude  = float(request.GET.get('latitude', None))
            position  = (latitude,longitude)
            condition = (
                Q(latitude__range  = (latitude - 0.01, latitude + 0.01)) |
                Q(longitude__range = (longitude - 0.015, longitude + 0.015))
            )

            convenience_infos = (
                ConvenienceInfo
                .objects
                .filter(condition)
            )
            near_convenience_infos = [info for info in convenience_infos
                                      if haversine(position, (info.latitude, info.longitude)) <= 2]

            safety_infos = (
                SafetyInfo
                .objects
                .filter(condition)
            )
            near_safety_infos = [info for info in safety_infos
                                 if haversine(position, (info.latitude, info.longitude)) <= 2]

            education_infos = (
                EducationInfo
                .objects
                .filter(condition)
            )
            near_education_infos = [info for info in education_infos
                                    if haversine(position, (info.latitude, info.longitude)) <= 2]