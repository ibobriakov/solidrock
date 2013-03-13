from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from main.utils import patch_model


class UserOverride:
    USER_TYPE_CHOICES = (
        (0, 'Job Seeker'),
        (1, 'Employer'),
    )
    user_type = models.IntegerField(verbose_name=_('user type'), choices=USER_TYPE_CHOICES, default=0)
    email = models.EmailField(verbose_name=_('e-mail address'), unique=True)
    is_email_active = models.EmailField(verbose_name=_('is e-mail active'), default=False)

    def save(self, *args, **kwargs):
        if self.username != self.email:
            self.username = self.email
        return self.save__overridden(*args, **kwargs)


patch_model(User, UserOverride)


class Employer(models.Model):
    user = models.OneToOneField('auth.User')


class JobSeeker(models.Model):
    user = models.OneToOneField('auth.User')

User.profile = property(lambda u:   Employer.objects.get_or_create(user=u)[0]
                                    if u.user_type == 1 else
                                    JobSeeker.objects.get_or_create(user=u)[0])