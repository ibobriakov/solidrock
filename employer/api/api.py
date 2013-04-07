from django.forms.models import modelform_factory
from tastypie import fields
from tastypie.authentication import SessionAuthentication
from tastypie.resources import ModelResource
from employer.api.validation import JobResourceValidation
from main.api import ResourceLabelSchemaMixin, ResourceFieldsOrderSchemaMixin, ResourceRelatedFieldsUrlSchemaMixin
from ..models import JobLocation, Hour, EmploymentType, SpecialCondition, JobUploadDocumentType,\
    Job, Essential, Desireable, JobCategory, JobSubCategory, JobUploadDocument,\
    JobSelectedCategory, JobSelectedSubCategory, JobExecutivePositions
from userprofile.api import AuthorizationWithObjectPermissions

__author__ = 'ir4y'


def get_resource_fabric(model_class):
    class ModelResourceWithName(ModelResource):
        name = fields.CharField(readonly=True)

        def dehydrate_name(self, bundle):
            return bundle.obj.__unicode__()

    class ModelGetResource(ModelResourceWithName):
        class Meta:
            resource_name = model_class.__name__.lower()
            queryset = model_class.objects.all()
            allowed_methods = ('get',)
    return ModelGetResource

LocationResource = get_resource_fabric(JobLocation)
HourResource = get_resource_fabric(Hour)
EmploymentTypeResource = get_resource_fabric(EmploymentType)
SpecialConditionResource = get_resource_fabric(SpecialCondition)
JobCategoryResource = get_resource_fabric(JobCategory)
JobSubCategoryResource = get_resource_fabric(JobSubCategory)
JobUploadDocumentTypeResource = get_resource_fabric(JobUploadDocumentType)
JobExecutivePositionsResource = get_resource_fabric(JobExecutivePositions)


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
    executive_positions = fields.ToOneField(JobExecutivePositionsResource, 'executive_positions',
                                            blank=True, null=True)

    essential_set = fields.ToManyField(EssentialResource, 'essential_set', full=True, null=True)
    desireable_set = fields.ToManyField(DesireableResource, 'desireable_set', full=True, null=True)

    # TODO fix append error or remove permanently if is doesn't need any more
    # categories = fields.ToManyField(JobCategoryResource, 'categories', full=True, null=True)
    # sub_categories = fields.ToManyField(JobSubCategoryResource, 'sub_categories', full=True, null=True)

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
        validation = JobResourceValidation(form_class=modelform_factory(Job))


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
    category = fields.ToOneField(JobCategoryResource, 'category')

    class Meta:
        queryset = JobSelectedCategory.objects.all()
        authentication = SessionAuthentication()
        authorization = AuthorizationWithObjectPermissions()


class JobSelectedSubCategoryResource(ModelResource):
    job = fields.ToOneField('employer.api.JobResource', 'job')
    subcategory = fields.ToOneField(JobSubCategoryResource, 'subcategory')

    class Meta:
        queryset = JobSelectedSubCategory.objects.all()
        authentication = SessionAuthentication()
        authorization = AuthorizationWithObjectPermissions()