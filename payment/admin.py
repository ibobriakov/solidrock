from django.contrib import admin
from models import Transaction, Order, AdPackageHistory, Subscription, SubscriptionType, AdPackageType, AdPackage

__author__ = 'ir4y'


class OrderInline(admin.TabularInline):
    model = Order


class TransactionAdmin(admin.ModelAdmin):
    list_display = ('datetime', 'owner', 'amount', 'approved', 'operation_result', )
    inlines = [OrderInline, ]


class OrderAdmin(admin.ModelAdmin):
    list_display = ('datetime', 'owner', 'order_object', )


class AdPackageHistoryAdmin(admin.ModelAdmin):
    list_display = ('datetime', 'owner', 'ad_count', 'get_action_display', )


admin.site.register(Subscription)
admin.site.register(SubscriptionType)
admin.site.register(AdPackageType)
admin.site.register(AdPackage)
admin.site.register(Transaction, TransactionAdmin)
admin.site.register(Order,OrderAdmin)
admin.site.register(AdPackageHistory, AdPackageHistoryAdmin)
