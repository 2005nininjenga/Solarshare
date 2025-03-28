from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SubscriptionPlanViewSet

router = DefaultRouter()
router.register('', SubscriptionPlanViewSet, basename='plan')

urlpatterns = [
    path('', include(router.urls)),
]
