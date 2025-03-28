from rest_framework import viewsets
from .models import SubscriptionPlan
from .serializers import SubscriptionPlanSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class SubscriptionPlanViewSet(viewsets.ModelViewSet):
    queryset = SubscriptionPlan.objects.all()
    serializer_class = SubscriptionPlanSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
