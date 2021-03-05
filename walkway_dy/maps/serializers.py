from rest_framework import serializers
from .models import WalkwayLocation


class WalkwaySerializer(serializers.ModelSerializer):

    class Meta:
        model = WalkwayLocation
        fields = '__all__'