from django.contrib import admin
from models import Transaction

__author__ = 'ir4y'


class TransactionAdmin(admin.ModelAdmin):
    list_display = ('datetime', 'owner', 'amount', 'approved', 'operation_result')

admin.site.register(Transaction, TransactionAdmin)
