from employer.api import get_resource_fabric
from models import SubscriptionType, AdPackageType

__author__ = 'jackdevil'

__all__ = ['SubscriptionTypeResource', 'AdPackageTypeResource']

SubscriptionTypeResource = get_resource_fabric(SubscriptionType)
AdPackageTypeResource = get_resource_fabric(AdPackageType)

