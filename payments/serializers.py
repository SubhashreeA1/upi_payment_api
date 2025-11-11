from rest_framework import serializers
from .models import Transaction

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['id', 'user', 'upi_id', 'amount', 'status', 'created_at']
        read_only_fields = ['id', 'status', 'created_at']
