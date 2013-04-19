from django.contrib import admin
from models import Transaction, AdPackageHistory, Subscription, SubscriptionType, AdPackageType

__author__ = 'ir4y'


class TransactionAdmin(admin.ModelAdmin):
    list_display = ('datetime', 'owner', 'amount', 'approved', 'operation_result', )


class AdPackageHistoryAdmin(admin.ModelAdmin):
    list_display = ('datetime', 'owner', 'ad_count', 'get_action_display', )


admin.site.register(Subscription)
admin.site.register(SubscriptionType)
admin.site.register(AdPackageType)
admin.site.register(Transaction, TransactionAdmin)
admin.site.register(AdPackageHistory, AdPackageHistoryAdmin)
