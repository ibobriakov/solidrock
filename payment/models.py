from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.db.models.signals import post_save
from employer.models import Job
from utils import buy_job, buy_ad_package, buy_subcription


class Transaction(models.Model):
    owner = models.ForeignKey('auth.User')
    datetime = models.DateTimeField(auto_now_add=True)
    amount = models.PositiveIntegerField()
    approved = models.BooleanField(default=False)
    result = models.PositiveIntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    error_code = models.PositiveIntegerField(blank=True, null=True)

    def operation_result(self):
        if self.approved:
            return self.result
        else:
            return "{0} {1}".format(self.error_code, self.error)

    class Meta:
        ordering = ("-datetime", )


class Order(models.Model):
    datetime = models.DateTimeField(auto_now_add=True)
    amount = models.PositiveIntegerField()
    transaction = models.ForeignKey('payment.Transaction')
    owner = models.ForeignKey('auth.User')
    approved = models.BooleanField(default=False)
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    order_object = generic.GenericForeignKey('content_type', 'object_id')


class SubscriptionType(models.Model):
    name = models.CharField(max_length=50)
    prolongation = models.PositiveIntegerField()
    cost = models.PositiveIntegerField()
    promo = models.TextField()

    def __unicode__(self):
        return self.name


class Subscription(models.Model):
    owner = models.ForeignKey('auth.User')
    start_date = models.DateTimeField(auto_now_add=True)
    finish_date = models.DateTimeField()
    type = models.ForeignKey('payment.SubscriptionType')

    def __unicode__(self):
        return "{0}".format(self.owner)


class AdPackageType(models.Model):
    name = models.CharField(max_length=50)
    ad_count = models.PositiveIntegerField()
    cost = models.PositiveIntegerField()
    promo = models.TextField()
    default = models.BooleanField(verbose_name='Offer default', default=False)

    def __unicode__(self):
        return self.name


class AdPackage(models.Model):
    owner = models.ForeignKey('auth.User')
    count = models.PositiveIntegerField()
    type = models.ForeignKey('payment.AdPackageType')
    start_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return "{0}".format(self.owner)


class AdPackageHistory(models.Model):
    ACTION_CHOICES = (
        (0, "purchase"),
        (1, "post job"),
    )
    datetime = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey('auth.User')
    ad_count = models.PositiveIntegerField()
    action = models.PositiveIntegerField(choices=ACTION_CHOICES)

    class Meta:
        ordering = ("-datetime", )


job_content_type = ContentType.objects.get_for_model(Job)
ad_package_content_type = ContentType.objects.get_for_model(AdPackageType)
subscribe_content_type = ContentType.objects.get_for_model(SubscriptionType)


def after_order_save(instance, created, **kwargs):
    # todo check if it has already approved
    if not created and instance.approved:
        if instance.content_type == ad_package_content_type:
            buy_ad_package(instance.order_object, instance.owner)
        elif instance.content_type == subscribe_content_type:
            buy_subcription(instance.order_object, instance.owner)
        elif instance.content_type == job_content_type:
            buy_job(instance.order_object, instance.owner)


post_save.connect(after_order_save,Order)