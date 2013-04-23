import datetime

__author__ = 'ir4y'


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

