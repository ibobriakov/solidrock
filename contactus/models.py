from django.db import models


class Feedback(models.Model):
    PRIORITY_CHOICES = (
        (0, 'Cannot proceed without assistance'),
        (1, 'Can proceed and require assistance within 48 hours'),
    )
    name = models.CharField(verbose_name="Name", max_length=255)
    email = models.EmailField(verbose_name="Email")
    subject = models.CharField(verbose_name="Subject", max_length=100)
    priority = models.IntegerField(verbose_name="Priority", choices=PRIORITY_CHOICES, default=0)
    message = models.TextField(verbose_name="Message")

    def __unicode__(self):
        return "{0} from {1}".format(self.subject, self.name)
