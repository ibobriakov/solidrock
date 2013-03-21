from django.core.exceptions import ValidationError
from django.db import models
from userprofile.models.fields import PhoneField


class JobLocation(models.Model):
    location = models.CharField(verbose_name="Job Location", max_length=150)

    def __unicode__(self):
        return self.location


class SalaryRange(models.Model):
    salary_range = models.CharField(verbose_name="Salary Range", max_length=100)

    def __unicode__(self):
        return self.salary_range


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
    owner = models.ForeignKey('auth.User')
    name = models.CharField(verbose_name="Name This Job Posting", max_length=100)
    title = models.CharField(verbose_name="Job Title", max_length=100)
    description = models.TextField(verbose_name="Description")
    location = models.ForeignKey('employer.JobLocation', verbose_name="Job Location")
    award = models.CharField(verbose_name="Applicabla Award (if applicable)", max_length=100, blank=True, null=True)
    salary_range = models.ForeignKey('employer.SalaryRange', verbose_name="Salary Range", blank=True, null=True)
    hours = models.ForeignKey('employer.Hour', verbose_name="Hours")
    employment_type = models.ForeignKey('employer.EmploymentType', verbose_name="Type of Employment")
    special_conditions = models.ForeignKey('employer.SpecialCondition', verbose_name="Special Condition",
                                           blank=True, null=True)
    other_conditions = models.CharField(verbose_name='If "Other" Please Indicate', max_length=255,
                                        blank=True, null=True)
    open_date = models.DateField(verbose_name="Date Job Listing Opens", blank=True, null=True)
    end_date = models.DateField(verbose_name="Date Job Listing Ends", blank=True, null=True)

    contact_name = models.CharField(verbose_name='Name', max_length=150)
    contact_phone = PhoneField(verbose_name='Phone', blank=True, null=True, default='')
    contact_email = models.EmailField(verbose_name='Email')

    categories = models.ManyToManyField('employer.JobCategory', through='employer.JobSelectedCategory')
    sub_categories = models.ManyToManyField('employer.JobSubCategory', through='employer.JobSelectedCategory')

    def __unicode__(self):
        return self.name


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
    category = models.ForeignKey('employer.JobCategory', verbose_name="Category", related_name='subcategories_set')
    sub_category_name = models.CharField(verbose_name="Sub Category Name", max_length=100)

    def __unicode__(self):
        return self.sub_category_name


class JobSelectedCategory(models.Model):
    job = models.ForeignKey('employer.Job')
    category = models.ForeignKey('employer.JobCategory')
    sub_category = models.ForeignKey('employer.JobSubCategory')

    def clean(self):
        if self.sub_category not in self.category.jobsubcategory_set.all():
            raise  ValidationError("Category and subcategory miss match")
