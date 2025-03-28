from rest_framework import serializers
from .models import BillingRecord

class BillingRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = BillingRecord
        fields = '__all__'
        read_only_fields = ['user', 'payment_date']
