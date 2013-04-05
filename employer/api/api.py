from django.forms.models import modelform_factory
from tastypie import fields
from tastypie.authentication import SessionAuthentication
from tastypie.resources import ModelResource
from employer.api.validation import EmployerResourceValidation
from main.api import ResourceLabelSchemaMixin, ResourceFieldsOrderSchemaMixin, ResourceRelatedFieldsUrlSchemaMixin
from ..models import JobLocation, Hour, EmploymentType, SpecialCondition, JobUploadDocumentType,\
    Job, Essential, Desireable, JobCategory, JobSubCategory, JobUploadDocument, JobSelectedCategory
from userprofile.api import AuthorizationWithObjectPermissions

__author__ = 'ir4y'


class ModelResourceWithName(ModelResource):
    name = fields.CharField(readonly=True)

    def dehydrate_name(self, bundle):
        return bundle.obj.__unicode__()


class LocationResource(ModelResourceWithName):

    class Meta:
        queryset = JobLocation.objects.all()
        allowed_methods = ('get',)


class HourResource(ModelResourceWithName):
    class Meta:
        queryset = Hour.objects.all()
        allowed_methods = ('get',)


class EmploymentTypeResource(ModelResourceWithName):
    class Meta:
        queryset = EmploymentType.objects.all()
        allowed_methods = ('get',)


class SpecialConditionResource(ModelResourceWithName):
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
        authorization = AuthorizationWithObjectPermissions()


class DesireableResource(ModelResource):
    job = fields.ToOneField('employer.api.JobResource', 'job')

    def get_object_list(self, request):
        query_set = super(DesireableResource, self).get_object_list(request)
        return query_set.filter(job__owner=request.user)

    class Meta:
        queryset = Desireable.objects.all()
        authorization = AuthorizationWithObjectPermissions()


class JobResource(ResourceFieldsOrderSchemaMixin, ResourceLabelSchemaMixin,
                  ResourceRelatedFieldsUrlSchemaMixin, ModelResource):
    location = fields.ToOneField(LocationResource, 'location', blank=True, null=True)
    hours = fields.ToOneField(HourResource, 'hours', blank=True, null=True)
    employment_type = fields.ToOneField(EmploymentTypeResource, 'employment_type', blank=True, null=True)
    special_conditions = fields.ToOneField(SpecialConditionResource, 'special_conditions',
                                           blank=True, null=True)

    essential_set = fields.ToManyField(EssentialResource, 'essential_set', full=True, null=True)
    desireable_set = fields.ToManyField(DesireableResource, 'desireable_set', full=True, null=True)

    def get_object_list(self, request):
        query_set = super(JobResource, self).get_object_list(request)
        return query_set.filter(owner=request.user)

    def hydrate(self, bundle):
        bundle.obj.user = bundle.request.user
        for item in bundle.data['essential_set']:
            item['job'] = bundle.data['resource_uri']
        for item in bundle.data['desireable_set']:
            item['job'] = bundle.data['resource_uri']
        return bundle

    class Meta:
        queryset = Job.objects.all()
        resource_name = 'job'
        always_return_data = True
        authentication = SessionAuthentication()
        authorization = AuthorizationWithObjectPermissions()
        validation = EmployerResourceValidation(form_class=modelform_factory(Job))


class JobCategoryResource(ResourceRelatedFieldsUrlSchemaMixin, ModelResourceWithName):
    subcategories_set = fields.ToManyField('employer.api.JobSubCategoryResource', 'subcategories_set',
                                           full=True, blank=True, null=True)

    class Meta:
        queryset = JobCategory.objects.all()
        allowed_methods = ('get',)


class JobSubCategoryResource(ResourceRelatedFieldsUrlSchemaMixin, ModelResourceWithName):
    category = fields.ToOneField('employer.api.JobCategoryResource', 'category')

    class Meta:
        queryset = JobSubCategory.objects.all()
        allowed_methods = ('get',)


class JobUploadDocumentTypeResource(ModelResource):
    class Meta:
        queryset = JobUploadDocumentType.objects.all()
        allowed_methods = ('get',)


class JobUploadDocumentResource(ModelResource):
    job = fields.ToOneField('employer.api.JobResource', 'job')
    document_type = fields.ToOneField('employer.api.JobUploadDocumentTypeResource', 'document_type', full=True)
    document_type_name = fields.CharField(readonly=True)
    file_name = fields.CharField(readonly=True)

    def dehydrate_document_type_name(self, bundle):
        return bundle.obj.document_type.__unicode__()

    def dehydrate_file_name(self, bundle):
        return bundle.obj.__unicode__()

    class Meta:
        queryset = JobUploadDocument.objects.all()
        allowed_methods = ('get', 'delete')
        resource_name = 'job_upload_document'
        authentication = SessionAuthentication()
        authorization = AuthorizationWithObjectPermissions()


class JobSelectedCategoryResource(ModelResource):
    job = fields.ToOneField('employer.api.JobResource', 'job')
    category = fields.ToOneField('employer.api.JobCategoryResource', 'category')
    subcategories_set = fields.ToManyField('employer.api.JobSubCategoryResource', 'subcategories_set',
                                           full=True, blank=True, null=True)

    class Meta:
        queryset = JobSelectedCategory.objects.all()
        authentication = SessionAuthentication()
        authorization = AuthorizationWithObjectPermissions()
