from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
import json
import logging

logger = logging.getLogger(__name__)

@api_view(['POST'])
def transaction_webhook(request):
    try:
        data = json.loads(request.body)
        transaction_id = data.get("transaction_id")
        status = data.get("status")

        if not transaction_id or not status:
            return Response({"error": "Missing transaction_id or status"}, status=400)

        # Log and process webhook
        logger.info(f"Webhook received: Transaction {transaction_id} is now {status}")

        return Response({"message": "Webhook received"}, status=200)

    except Exception as e:
        logger.error(f"Error processing webhook: {str(e)}")
        return Response({"error": "Internal Server Error"}, status=500)
