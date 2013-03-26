from django.forms.models import modelform_factory
from tastypie import fields
from tastypie.authentication import SessionAuthentication
from tastypie.resources import ModelResource
from tastypie.validation import FormValidation
from main.api import ResourceLabelSchemaMixin, ResourceFieldsOrderSchemaMixin, ResourceRelatedFieldsUrlSchemaMixin
from models import JobLocation, SalaryRange, Hour, EmploymentType, SpecialCondition
from models import Job, Essential, Desireable, JobCategory, JobSubCategory
from userprofile.api import AuthorizationWithObjectPermissions

__author__ = 'ir4y'
__all__ = ['JobResource', 'LocationResource', 'SalaryRangeResource', 'HourResource',
           'EmploymentTypeResource', 'SpecialConditionResource', 'EssentialResource', 'DesireableResource',
           'JobCategoryResource', 'JobSubCategoryResource']


class LocationResource(ModelResource):
    class Meta:
        queryset = JobLocation.objects.all()
        allowed_methods = ('get',)


class SalaryRangeResource(ModelResource):
    class Meta:
        queryset = SalaryRange.objects.all()
        allowed_methods = ('get',)


class HourResource(ModelResource):
    class Meta:
        queryset = Hour.objects.all()
        allowed_methods = ('get',)


class EmploymentTypeResource(ModelResource):
    class Meta:
        queryset = EmploymentType.objects.all()
        allowed_methods = ('get',)


class SpecialConditionResource(ModelResource):
    class Meta:
        queryset = SpecialCondition.objects.all()
        allowed_methods = ('get',)


class EssentialResource(ModelResource):
    job = fields.ToOneField('employer.api.JobResource', 'job')

    def get_object_list(self, request):
        query_set = super(EssentialResource, self).get_object_list(request)
        return query_set.filter(job__owner=request.user)

    class Meta:
        queryset = Essential.objects.all()


class DesireableResource(ModelResource):
    job = fields.ToOneField('employer.api.JobResource', 'job')

    def get_object_list(self, request):
        query_set = super(DesireableResource, self).get_object_list(request)
        return query_set.filter(job__owner=request.user)

    class Meta:
        queryset = Desireable.objects.all()


class JobResource(ResourceFieldsOrderSchemaMixin, ResourceLabelSchemaMixin,
                  ResourceRelatedFieldsUrlSchemaMixin, ModelResource):
    location = fields.ToOneField(LocationResource, 'location', full=True)
    salary_range = fields.ToOneField(SalaryRangeResource, 'salary_range', blank=True, null=True, full=True)
    hours = fields.ToOneField(HourResource, 'hours', full=True)
    employment_type = fields.ToOneField(EmploymentTypeResource, 'employment_type', full=True)
    special_conditions = fields.ToOneField(SpecialConditionResource, 'special_conditions',
                                           blank=True, null=True, full=True)

    essential_set = fields.ToManyField(EssentialResource, 'essential_set', full=True)
    desireable_set = fields.ToManyField(DesireableResource, 'desireable_set', full=True)

    def get_object_list(self, request):
        query_set = super(JobResource, self).get_object_list(request)
        return query_set.filter(owner=request.user)

    def hydrate(self, bundle):
        bundle.obj.user = bundle.request.user
        return bundle

    class Meta:
        queryset = Job.objects.all()
        resource_name = 'job'
        always_return_data = True
        authentication = SessionAuthentication()
        authorization = AuthorizationWithObjectPermissions()
        validation = FormValidation(form_class=modelform_factory(Job))


class JobCategoryResource(ResourceRelatedFieldsUrlSchemaMixin, ModelResource):
    subcategories_set = fields.ToManyField('employer.api.JobSubCategoryResource', 'subcategories_set',
                                           full=True, blank=True, null=True)

    class Meta:
        queryset = JobCategory.objects.all()
        allowed_methods = ('get',)


class JobSubCategoryResource(ResourceRelatedFieldsUrlSchemaMixin, ModelResource):
    category = fields.ToOneField('employer.api.JobCategoryResource', 'category')

    class Meta:
        queryset = JobSubCategory.objects.all()
        allowed_methods = ('get',)