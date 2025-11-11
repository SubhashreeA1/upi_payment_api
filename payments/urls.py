from django.urls import path
from .views import InitiateTransactionView, CheckTransactionStatusView, ProcessPaymentView

urlpatterns = [
    path('initiate/', InitiateTransactionView.as_view(), name='initiate_transaction'),
    path('status/<uuid:transaction_id>/', CheckTransactionStatusView.as_view(), name='check_status'),
    path('process/<uuid:transaction_id>/', ProcessPaymentView.as_view(), name='process_payment'),
]
