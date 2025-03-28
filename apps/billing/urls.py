from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BillingRecordViewSet

router = DefaultRouter()
router.register(r'billing-records', BillingRecordViewSet, basename='billingrecord')

urlpatterns = [
    path('', include(router.urls)),
]
