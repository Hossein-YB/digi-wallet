from django.contrib import admin
from django.contrib.admin import register

from .models import Transaction, UserBalance


@register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('user', 'transaction_type', 'amount', 'datetime_created')
    list_filter = ('transaction_type',)
    search_fields = ("user__username", )


@register(UserBalance)
class UserBalanceAdmin(admin.ModelAdmin):
    list_display = ('user', 'balance', 'datetime_created',)
    search_fields = ("user__username", )


