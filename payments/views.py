from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from django.views import View
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import Transaction
from .tasks import process_transaction
from .serializers import TransactionSerializer
import random
# Create your views here.
class InitiateTransactionView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response({"message": "Transaction initiated", "transaction": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CheckTransactionStatusView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, transaction_id):
        try:
            transaction = Transaction.objects.get(id=transaction_id, user=request.user)
            return Response({"transaction_id": transaction.id, "status": transaction.status}, status=status.HTTP_200_OK)
        except Transaction.DoesNotExist:
            return Response({"error": "Transaction not found"}, status=status.HTTP_404_NOT_FOUND)

class ProcessPaymentView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, transaction_id):
        try:
            transaction = Transaction.objects.get(id=transaction_id, user=request.user)

            if transaction.status != "PENDING":
                return Response({"message": "Transaction already processed"}, status=status.HTTP_400_BAD_REQUEST)

            # Enqueue transaction processing task asynchronously
            process_transaction.delay(str(transaction.id))

            return Response({"message": "Transaction is being processed asynchronously"}, status=status.HTTP_202_ACCEPTED)

        except Transaction.DoesNotExist:
            return Response({"error": "Transaction not found"}, status=status.HTTP_404_NOT_FOUND)
            