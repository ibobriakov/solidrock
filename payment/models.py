from django.db import models


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
        return "{0}-{1} for {3}".format(self.start_date, self.finish_date, self.owner)


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
        return "{0}-{1} for {3}".format(self.type, self.count, self.owner)


class AdPackageHistory(models.Model):
    ACTION_CHOICES = (
        (0, "purchase"),
        (1, "post job"),
    )
    datetime = models.DateTimeField(auto_now_add=True)
    owner = models.OneToOneField('auth.User')
    ad_count = models.PositiveIntegerField()
    action = models.PositiveIntegerField(choices=ACTION_CHOICES)

    class Meta:
        ordering = ("-datetime", )
