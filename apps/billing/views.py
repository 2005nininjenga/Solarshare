from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import BillingRecord
from .serializers import BillingRecordSerializer

class BillingRecordViewSet(viewsets.ModelViewSet):
    serializer_class = BillingRecordSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return BillingRecord.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
