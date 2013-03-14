from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from main.utils import patch_model
from fields import PhoneField
from mixins import AddressMixin


class UserOverride:
    USER_TYPE_CHOICES = (
        (0, 'Job Seeker'),
        (1, 'Employer'),
    )
    user_type = models.IntegerField(verbose_name=_('user type'), choices=USER_TYPE_CHOICES, default=0)
    email = models.EmailField(verbose_name=_('e-mail address'), unique=True)
    is_email_active = models.BooleanField(verbose_name=_('is e-mail active'), default=False)

    def save(self, *args, **kwargs):
        if self.username != self.email:
            self.username = self.email
        return self.save__overridden(*args, **kwargs)

    class Meta:
        app_label = 'userprofile'


patch_model(User, UserOverride)


class Employer(models.Model):
    user = models.OneToOneField('auth.User')
    company = models.CharField(verbose_name=_('Company Name'), max_length=255, db_index=True, unique=True)
    phone = PhoneField(verbose_name=_('phone number'))

    class Meta:
        app_label = 'userprofile'


class JobSeeker(models.Model):
    user = models.OneToOneField('auth.User')

    @property
    def first_name(self):
        return self.user.first_name

    @property
    def last_name(self):
        return self.user.last_name

    class Meta:
        app_label = 'userprofile'


class JobSeekerInformation(AddressMixin, models.Model):
    user = models.OneToOneField('userprofile.Employer')
    photo = models.ImageField(verbose_name=_("Profile picture(optional)"), blank=True, null=True)
    home_phone = PhoneField(verbose_name=_("Home Phone Number"), blank=True)
    daytime_phone = PhoneField(verbose_name=_("Daytime Phone Number"), blank=True)
    mobile_phone = PhoneField(verbose_name=_("Mobile Phone Number"), blank=True)
    email = models.EmailField(_('Email Address'), blank=True)
    can_contact_at_work = models.BooleanField(verbose_name=_("Can Potential employers contact you at work?"),
                                              default=False)
    is_australian = models.BooleanField(verbose_name=_("Are you an Australian Citizen/Permanent Resident?"),
                                        default=False)
    have_visa = models.BooleanField(verbose_name=_("If no do you have a working visa?"),
                                    default=False)
    is_driver = models.BooleanField(verbose_name=_("Do you have a current driver's licence?"),
                                    default=False)

    class Meta:
        app_label = 'userprofile'


class JobSeekerCurrentEmployment(AddressMixin, models.Model):
    user = models.OneToOneField('userprofile.Employer')
    name = models.CharField(verbose_name="Name of Employer", max_length=255, blank=True)
    position_title = models.CharField(verbose_name="Position Title", max_length=255, blank=True)
    date_commenced = models.DateField(verbose_name="Date Commenced", blank=True)
    department = models.CharField(verbose_name="Department/Section", max_length=255, blank=True)
    brief = models.TextField(verbose_name="Brief Description of Duties", blank=True)
    job_type = models.CharField(verbose_name="Fulltime, Parttime or Casual", max_length=255, blank=True)
    last_day_of_service = models.CharField(verbose_name="Last Day of Service", max_length=255, blank=True)
    leaving_reason = models.TextField(verbose_name="Reson for Leaving", blank=True)

    class Meta:
        app_label = 'userprofile'


User.profile = property(lambda u:   Employer.objects.get(user=u)[0]
                                    if u.user_type == 1 else
                                    JobSeeker.objects.get(user=u)[0])