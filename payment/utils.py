__author__ = 'ir4y'


def is_ads_already_paid(user):
    from payment.models import Subscription, AdPackage
    return (Subscription.objects.filter(owner=user).count() + AdPackage.objects.filter(owner=user).count()) > 0


def buy_job(job,user):
    pass


def buy_ad_package(package,user):
    pass


def buy_subcription(subscripion,user):
    pass

