from tastypie import fields
from tastypie.resources import ModelResource
from employer.api import get_resource_fabric
from models import SubscriptionType, AdPackageType, AdPackage, Subscription

__author__ = 'jackdevil'

__all__ = ['SubscriptionTypeResource', 'AdPackageTypeResource',
           'SubscriptionResource', 'AdPackageResource']

SubscriptionTypeResource = get_resource_fabric(SubscriptionType)
AdPackageTypeResource = get_resource_fabric(AdPackageType)
# SubscriptionResource = get_resource_fabric(Subscription)
#AdPackageResource = get_resource_fabric(AdPackage)


class SubscriptionResource(ModelResource):
    type = fields.ToOneField('payment.api.SubscriptionTypeResource', 'type', full=True)

    class Meta:
        queryset = Subscription.objects.all()


class AdPackageResource (ModelResource):
    type = fields.ToOneField('payment.api.AdPackageTypeResource', 'type', full=True)

    class Meta:
        queryset = AdPackage.objects.all()