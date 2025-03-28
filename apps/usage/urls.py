from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EnergyUsageViewSet

router = DefaultRouter()
router.register('', EnergyUsageViewSet, basename='usage')

urlpatterns = [
    path('', include(router.urls)),
]
