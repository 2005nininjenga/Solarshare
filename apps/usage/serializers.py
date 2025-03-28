from rest_framework import serializers
from .models import EnergyUsage

class EnergyUsageSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnergyUsage
        fields = '__all__'
