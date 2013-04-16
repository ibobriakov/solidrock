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