from django.core.exceptions import ValidationError
from django.db import models
from django.db.models.signals import post_save, post_delete, m2m_changed
from django.dispatch import receiver
from search.tasks import update_index
from userprofile.models.fields import PhoneField


class JobExecutivePositions(models.Model):
    position_name = models.CharField(verbose_name="Executive Position", max_length=150)

    def __unicode__(self):
        return self.position_name


class JobLocation(models.Model):
    location = models.CharField(verbose_name="Job Location", max_length=150)

    def __unicode__(self):
        return self.location


class JobArea(models.Model):
    area = models.CharField(verbose_name="Job Area", max_length=150)

    def __unicode__(self):
        return self.area


class Hour(models.Model):
    hour = models.CharField(verbose_name="Hours", max_length=100)

    def __unicode__(self):
        return self.hour


class EmploymentType(models.Model):
    type_name = models.CharField(verbose_name="Type of Employment", max_length=100)

    def __unicode__(self):
        return self.type_name


class SpecialCondition(models.Model):
    special_condition = models.CharField(verbose_name="Special Condition", max_length=100)

    def __unicode__(self):
        return self.special_condition


class Job(models.Model):
    REQUIRED_FIELDS = ('name', 'title', 'description', 'location', 'hours', 'employment_type',
                       'contact_name', 'contact_email', 'contact_phone',)
    # Because we need all information about hob preloaded
    # We need this tuple of required fields for validation
    owner = models.ForeignKey('auth.User')
    name = models.CharField(verbose_name="Name This Job Posting", max_length=100,
                            blank=True, null=True)
    title = models.CharField(verbose_name="Job Title", max_length=100,
                             blank=True, null=True)
    description = models.TextField(verbose_name="Description",
                                   blank=True, null=True)
    location = models.ForeignKey('employer.JobLocation', verbose_name="Job Location",
                                 blank=True, null=True)
    area = models.ForeignKey('employer.JobArea', verbose_name="Job Area",
                             blank=True, null=True)
    award = models.CharField(verbose_name="Applicabla Award (if applicable)", max_length=100,
                             blank=True, null=True)
    salary_range_min = models.IntegerField(verbose_name="Salary Range Min", max_length=100,
                                           blank=True, null=True)
    salary_range_max = models.IntegerField(verbose_name="Salary Range Max", max_length=100,
                                           blank=True, null=True)
    hours = models.ForeignKey('employer.Hour', verbose_name="Hours",
                              blank=True, null=True)
    employment_type = models.ForeignKey('employer.EmploymentType', verbose_name="Type of Employment",
                                        blank=True, null=True)
    special_conditions = models.ForeignKey('employer.SpecialCondition', verbose_name="Special Condition",
                                           blank=True, null=True)
    other_conditions = models.CharField(verbose_name='If "Other" Please Indicate', max_length=255,
                                        blank=True, null=True)
    open_date = models.DateField(verbose_name="Date Job Listing Opens",
                                 blank=True, null=True)
    end_date = models.DateField(verbose_name="Date Job Listing Ends",
                                blank=True, null=True)
    contact_name = models.CharField(verbose_name='Name', max_length=150,
                                    blank=True, null=True)
    contact_phone = PhoneField(verbose_name='Phone',
                               blank=True, null=True)
    contact_email = models.EmailField(verbose_name='Email',
                                      blank=True, null=True)
    featured_job = models.BooleanField(verbose_name="Mark as Featured Job", default=False)

    executive_positions = models.ForeignKey('employer.JobExecutivePositions', verbose_name='Executive Positions',
                                            blank=True, null=True)

    categories = models.ManyToManyField('employer.JobCategory', through='employer.JobSelectedCategory',
                                        blank=True, null=True)
    sub_categories = models.ManyToManyField('employer.JobSubCategory', through='employer.JobSelectedSubCategory',
                                            blank=True, null=True)

    def __unicode__(self):
        return "Job by {0}".format(self.owner)


class Essential(models.Model):
    job = models.ForeignKey('employer.Job')
    essential = models.CharField(verbose_name="Essential", max_length=100)

    def __unicode__(self):
        return self.essential


class Desireable(models.Model):
    job = models.ForeignKey('employer.Job')
    desireable = models.CharField(verbose_name="Desireable", max_length=100)

    def __unicode__(self):
        return self.desireable


class JobCategory(models.Model):
    category_name = models.CharField(verbose_name="Category Name", max_length=100)

    def __unicode__(self):
        return self.category_name


class JobSubCategory(models.Model):
    sub_category_name = models.CharField(verbose_name="Sub Category Name", max_length=100)

    def __unicode__(self):
        return self.sub_category_name


class JobSelectedCategory(models.Model):
    job = models.ForeignKey('employer.Job')
    category = models.ForeignKey('employer.JobCategory')


class JobSelectedSubCategory(models.Model):
    job = models.ForeignKey('employer.Job')
    sub_category = models.ForeignKey('employer.JobSubCategory')


class JobUploadDocumentType(models.Model):
    name = models.CharField(verbose_name="Document Type Name", max_length=100)
    max_count = models.IntegerField(default=-1)  # -1 for no limit

    def __unicode__(self):
        return self.name


class JobUploadDocument(models.Model):
    job = models.ForeignKey('employer.Job')
    document_type = models.ForeignKey('employer.JobUploadDocumentType')
    document = models.FileField(upload_to="job_document/%Y/%m/%d")

    def __unicode__(self):
        if self.document:
            return self.document.name.split('/')[-1]
        else:
            return super(JobUploadDocument, self).__unicode__()

    def clean(self):
        max_count = self.document_type.max_count
        if max_count > 0:
            if JobUploadDocument.objects.filter(job=self.job, document_type=self.document_type).count() >= max_count:
                raise  ValidationError("Too many Files for category {0}".format(self.document_type.__unicode__()))


def after_update(sender, **kwargs):
    if 'created' not in kwargs or not kwargs['created']:
        update_index.delay()
    else:
        instance = kwargs['instance']
        Essential.objects.create(job=instance, essential=' ')
        Desireable.objects.create(job=instance, desireable=' ')

receiver(post_save, sender=Job)(after_update)
receiver(post_delete, sender=Job)(after_update)
receiver(m2m_changed, sender=Job)(after_update)