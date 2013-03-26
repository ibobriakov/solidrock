from constance import config
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import post_save
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from main.utils import patch_model
from fields import PhoneField
from mixins import AddressMixin, SlugTraits


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


class Employer(AddressMixin, models.Model):
    user = models.OneToOneField('auth.User')
    logo = models.ImageField(verbose_name=_("Company Logo (optional)"), upload_to="company_logo/%Y/%m/%d",
                             blank=True, null=True)
    company = models.CharField(verbose_name=_('Company Name'), max_length=255, db_index=True, unique=True)
    abn_or_acn = models.CharField(verbose_name=_('ABN/ACN'), max_length=255, blank=True, null=True)
    business_phone = PhoneField(verbose_name=_('Business Phone'), blank=True, null=True)
    brief = models.TextField(verbose_name=_("Brief Description of Your Company"), blank=True, null=True)
    name = models.CharField(verbose_name=_('Name'), max_length=150, blank=True, null=True)
    phone = PhoneField(verbose_name=_('Phone'))
    email = models.EmailField(verbose_name=_('Email Address'), blank=True, null=True)
    agree = models.BooleanField(verbose_name=_('Do you agree to the Terms and Conditions?'), default=False)

    @property
    def avatar(self):
        return self.logo

    def url(self):
        return reverse('employer.profile.base')

    def __unicode__(self):
        return "Employer profile for {0}".format(self.company)

    class Meta:
        app_label = 'userprofile'


class JobSeeker(models.Model):
    user = models.OneToOneField('auth.User')

    def url(self):
        return reverse('job_seeker.profile.base')

    def __unicode__(self):
        return "Job Seeker profile for {0}".format(self.user.__unicode__())

    @property
    def first_name(self):
        return self.user.first_name

    @property
    def last_name(self):
        return self.user.last_name

    @property
    def avatar(self):
        return self.personal_information.photo

    class Meta:
        app_label = 'userprofile'


class JobSeekerInformation(AddressMixin, models.Model):
    job_seeker = models.OneToOneField('userprofile.JobSeeker', related_name='personal_information')
    photo = models.ImageField(verbose_name=_("Profile picture(optional)"), upload_to="user_photo/%Y/%m/%d",
                              blank=True, null=True)
    home_phone = PhoneField(verbose_name=_("Home Phone Number"), blank=True, null=True)
    daytime_phone = PhoneField(verbose_name=_("Daytime Phone Number"), blank=True, null=True)
    mobile_phone = PhoneField(verbose_name=_("Mobile Phone Number"), blank=True, null=True)
    email = models.EmailField(_('Email Address'), blank=True, null=True)
    can_contact_at_work = models.BooleanField(verbose_name=_("Can Potential employers contact you at work?"),
                                              default=False)
    is_australian = models.BooleanField(verbose_name=_("Are you an Australian Citizen/Permanent Resident?"),
                                        default=False)
    have_visa = models.BooleanField(verbose_name=_("If no do you have a working visa?"),
                                    default=False)
    is_driver = models.BooleanField(verbose_name=_("Do you have a current driver's licence?"),
                                    default=False)

    def get_photo_url(self):
        return self.photo.url if self.photo else config.DEFAULT_AVATAR

    def __unicode__(self):
        return "Job Seeker Information for {0}".format(self.job_seeker.__unicode__())

    class Meta:
        app_label = 'userprofile'


class JobSeekerCurrentEmployment(AddressMixin, models.Model):
    job_seeker = models.OneToOneField('userprofile.JobSeeker', related_name='current_employment')
    name = models.CharField(verbose_name="Name of Employer", max_length=255, blank=True, null=True)
    position_title = models.CharField(verbose_name="Position Title", max_length=255, blank=True, null=True)
    date_commenced = models.DateField(verbose_name="Date Commenced", blank=True, null=True)
    department = models.CharField(verbose_name="Department/Section", max_length=255, blank=True, null=True)
    brief = models.TextField(verbose_name="Brief Description of Duties", blank=True, null=True)
    job_type = models.CharField(verbose_name="Fulltime, Parttime or Casual", max_length=255, blank=True, null=True)
    last_day_of_service = models.CharField(verbose_name="Last Day of Service", max_length=255, blank=True, null=True)
    leaving_reason = models.TextField(verbose_name="Reson for Leaving", blank=True, null=True)

    def __unicode__(self):
        return "Job Seeker Current Employment for {0}".format(self.job_seeker.__unicode__())

    class Meta:
        app_label = 'userprofile'


class JobSeekerPreviousEmployment(AddressMixin, models.Model):
    job_seeker = models.ForeignKey('userprofile.JobSeeker', related_name='previous_employments_set')
    name = models.CharField(verbose_name="Name of Employer", max_length=255, blank=True, null=True)
    position_title = models.CharField(verbose_name="Position Title", max_length=255, blank=True, null=True)
    brief = models.TextField(verbose_name="Brief Description of Duties", blank=True, null=True)
    leaving_reason = models.TextField(verbose_name="Reson for Leaving", blank=True, null=True)

    def __unicode__(self):
        return "Job Seeker Previous Employment for {0}".format(self.job_seeker.__unicode__())

    class Meta:
        app_label = 'userprofile'


class JobSeekerEducationType(SlugTraits('type_name'), models.Model):
    type_name = models.CharField(verbose_name=_("Name of Education Type"), max_length=150)

    def __unicode__(self):
        return self.type_name

    class Meta:
        app_label = 'userprofile'


class JobSeekerEducation(models.Model):
    job_seeker = models.ForeignKey('userprofile.JobSeeker', related_name='educations_set')
    education_type = models.ForeignKey('userprofile.JobSeekerEducationType')
    value = models.CharField(max_length=255, blank=True, null=True)

    def __unicode__(self):
        return "Job Seeker Education {0} - {1} for {2}".format(self.education_type.__unicode__(),
                                                               self.value,
                                                               self.job_seeker.__unicode__())

    class Meta:
        app_label = 'userprofile'


class JobSeekerReferee(AddressMixin, models.Model):
    job_seeker = models.ForeignKey('userprofile.JobSeeker', related_name='referees_set')
    name = models.CharField(verbose_name="Name", max_length=255, blank=True, null=True)
    position_title = models.CharField(verbose_name="Position Title or Relationship", max_length=255, blank=True, null=True)
    phone_number = PhoneField(verbose_name=_("Phone Number"), blank=True, null=True)
    email = models.EmailField(_('Email Address'), blank=True, null=True)
    is_for_interview = \
        models.BooleanField(verbose_name=_("Are you willing for this to be approached prior to an interview ?"),
                            default=False)

    def __unicode__(self):
        return "Job Seeker Referee for {0}".format(self.job_seeker.__unicode__())

    class Meta:
        app_label = 'userprofile'


User.profile = property(lambda u: Employer.objects.get(user=u)
                        if u.user_type == 1 else
                        JobSeeker.objects.get(user=u))


def create_job_seeker_profile(instance, created, **kwargs):
    if created:
        JobSeekerInformation.objects.create(job_seeker=instance, email=instance.user.email)
        JobSeekerCurrentEmployment.objects.create(job_seeker=instance)
        JobSeekerPreviousEmployment.objects.create(job_seeker=instance)
        JobSeekerReferee.objects.create(job_seeker=instance)
        for education_type in JobSeekerEducationType.objects.all():
            JobSeekerEducation.objects.create(job_seeker=instance, education_type=education_type)


post_save.connect(create_job_seeker_profile, sender=JobSeeker)