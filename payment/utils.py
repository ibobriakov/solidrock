import copy
import datetime
from hashlib import md5
from django.conf import settings

__author__ = 'ir4y'


def calculate_secure_hash(data_dict, exclude=tuple()):
    secure_secret = copy.copy(settings.SECURE_SECRET)
    for key in sorted(data_dict.keys()):
        if key in exclude:
            continue
        secure_secret += data_dict[key]
    return md5(secure_secret).hexdigest().upper()


def has_subscription(user):
    from payment.models import Subscription
    return Subscription.objects.filter(owner=user, finish_date__gte=datetime.datetime.now()).count()>0


def has_ads_package(user):
    from payment.models import AdPackage
    return AdPackage.objects.filter(owner=user).exclude(count=0).count()>0


def is_ads_already_paid(user):
    return has_subscription(user) or has_ads_package(user)


def buy_job(job, user):
    from payment.models import AdPackage, AdPackageHistory
    if not has_subscription(user):
        if not has_ads_package(user):
            #todo handle error cant post job, but post
            pass
        package = AdPackage.objects.filter(owner=user).exclude(count=0)[0]
        package.count -= 1
        package.save()
        AdPackageHistory.objects.create(owner=user,
                                        ad_count=package.count,
                                        action=1)  # post job

    job.approved = True
    job.open_date = datetime.datetime.now().date()
    job.end_date = datetime.timedelta(days=30) + job.open_date
    job.save()


def buy_ad_package(package_type, user):
    from payment.models import AdPackage, AdPackageHistory
    AdPackage.objects.create(owner=user,
                             count=package_type.ad_count,
                             type=package_type)
    AdPackageHistory.objects.create(owner=user,
                                    ad_count=package_type.ad_count,
                                    action=0)  # purchase


def buy_subcription(subscription_type, user):
    from payment.models import Subscription
    Subscription.objects.create(owner=user,
                                finish_date=datetime.datetime.now() + \
                                            datetime.timedelta(days=subscription_type.prolongation),
                                type=subscription_type)

