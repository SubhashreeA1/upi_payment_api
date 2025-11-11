from celery import shared_task
from .models import Transaction
import requests
import time

@shared_task
def process_transaction(transaction_id):
    """
    Simulates real-time transaction processing.
    """
    try:
        transaction = Transaction.objects.get(id=transaction_id)
        
        # Simulate payment processing delay
        time.sleep(5)

        # Simulate settlement status
        transaction.status = "SUCCESS" if transaction.amount % 2 == 0 else "FAILED"
        transaction.save()

        # Trigger webhook
        webhook_url = "http://127.0.0.1:8000/api/webhooks/transaction-status/"
        payload = {"transaction_id": transaction_id, "status": transaction.status}
        requests.post(webhook_url, json=payload)

        return f"Transaction {transaction_id} processed successfully"
    
    except Transaction.DoesNotExist:
        return f"Transaction {transaction_id} not found"
