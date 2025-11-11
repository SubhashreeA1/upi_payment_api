from django.contrib import admin
from .models import Transaction

# Register your models here.

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'upi_id', 'amount', 'status', 'created_at', 'updated_at')
    list_filter = ('status', 'created_at')
    search_fields = ('upi_id', 'user__username')