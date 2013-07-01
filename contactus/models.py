from django.core.mail import send_mail
from django.db import models
from django.db.models.signals import post_save
from django.conf import settings
from django.template import loader, Context

class Feedback(models.Model):
    PRIORITY_CHOICES = (
        ('', '',),
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

def email_notify(instance, created, **kwargs):
    if created:
        template = loader.get_template("email/feedback.txt")
        email_text = template.render(Context({'feedback': instance}))
        send_mail('Solid Rock - Some one applied to your job!',
                  email_text, settings.EMAIL_HOST_USER, [settings.EMAIL_HOST_USER])

post_save.connect(email_notify,Feedback)
