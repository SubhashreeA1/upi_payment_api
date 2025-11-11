from django.urls import path
from .views import transaction_webhook

urlpatterns = [
    path('', transaction_webhook),
    path('transaction-status/', transaction_webhook, name='transaction-webhook'),
]
