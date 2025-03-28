from rest_framework import viewsets
from .models import EnergyUsage
from .serializers import EnergyUsageSerializer
from rest_framework.permissions import IsAuthenticated

class EnergyUsageViewSet(viewsets.ModelViewSet):
    serializer_class = EnergyUsageSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return EnergyUsage.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
