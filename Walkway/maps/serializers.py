from rest_framework import serializers
from .models import WalkwayLocation


class LocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = WalkwayLocation
        fields = '__all__'