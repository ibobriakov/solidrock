from django.forms.models import modelform_factory
from django.core.urlresolvers import reverse
from tastypie import fields
from tastypie.authentication import SessionAuthentication
from tastypie.resources import ModelResource
from employer.api.validation import JobResourceValidation
from main.api import ResourceLabelSchemaMixin, ResourceFieldsOrderSchemaMixin, ResourceRelatedFieldsUrlSchemaMixin
from ..models import JobLocation, Hour, EmploymentType, SpecialCondition, JobUploadDocumentType, \
    Job, Essential, Desireable, JobCategory, JobSubCategory, JobUploadDocument, \
    JobSelectedCategory, JobSelectedSubCategory, JobExecutivePositions, JobArea
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
JobAreaResource = get_resource_fabric(JobArea)
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
    area = fields.ToOneField(JobAreaResource, 'area', blank=True, null=True)
    hours = fields.ToOneField(HourResource, 'hours', blank=True, null=True)
    employment_type = fields.ToOneField(EmploymentTypeResource, 'employment_type', blank=True, null=True)
    special_conditions = fields.ToOneField(SpecialConditionResource, 'special_conditions',
                                           blank=True, null=True)
    executive_positions = fields.ToOneField(JobExecutivePositionsResource, 'executive_positions',
                                            blank=True, null=True)

    essential_set = fields.ToManyField(EssentialResource, 'essential_set', full=True, null=True)
    desireable_set = fields.ToManyField(DesireableResource, 'desireable_set', full=True, null=True)

    categories_set = fields.ToManyField('employer.api.JobSelectedCategoryResource',
                                        'jobselectedcategory_set', full=True, null=True)
    sub_categories_set = fields.ToManyField('employer.api.JobSelectedSubCategoryResource',
                                            'jobselectedsubcategory_set', full=True, null=True)

    jobuploaddocument_set = fields.ToManyField('employer.api.JobUploadDocumentResource',
                                               'jobuploaddocument_set', readonly=True, full=True)

    approved = fields.BooleanField('approved',readonly=True)
    archived =  fields.BooleanField('archived',readonly=True)


    def get_object_list(self, request):
        query_set = super(JobResource, self).get_object_list(request)
        return query_set.filter(owner=request.user)

    def hydrate(self, bundle):
        bundle.obj.owner = bundle.request.user
        return bundle

    class Meta:
        queryset = Job.objects.all()
        resource_name = 'job'
        always_return_data = True
        authentication = SessionAuthentication()
        authorization = AuthorizationWithObjectPermissions()
        validation = JobResourceValidation(form_class=modelform_factory(Job, exclude=('owner', )))
        filtering = {
                     'approved': ('exact',),
                     'archived': ('exact',)
                    }

class JobBannerResource(ModelResource):
    location = fields.CharField(readonly=True)
    open_date = fields.CharField('open_date')
    edit_url = fields.CharField(readonly=True)
    view_url = fields.CharField(readonly=True)

    def get_object_list(self, request):
        query_set = super(JobBannerResource, self).get_object_list(request)
        return query_set.filter(owner=request.user)

    def dehydrate_location(self, bundle):
        if bundle.obj.location_id:
            return bundle.obj.location.location

    def dehydrate_open_date(self,bundle):
        return  bundle.obj.open_date.strftime("%d %b %Y")

    def dehydrate_edit_url(self,bundle):
        return reverse('employer.job.edit', args=[bundle.obj.id])

    def dehydrate_view_url(self,bundle):
        return reverse('employer.job.view', args=[bundle.obj.id])

    class Meta:
        queryset = Job.objects.all()
        resource_name = 'jobbanner'
        always_return_data = True
        list_allowed_methods = ['get']
        fields = ['name', 'salary_range_min', 'open_date', 'approved', 'archived']
        filtering = {
                     'approved': ('exact',),
                     'archived': ('exact',)
                    }



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

    def lookup_kwargs_with_identifiers(self, bundle, kwargs):
        lookup_kwargs = super(JobSelectedCategoryResource, self).lookup_kwargs_with_identifiers(bundle,kwargs)
        if lookup_kwargs == {}:
            return {'pk': -1}
        return lookup_kwargs

    class Meta:
        queryset = JobSelectedCategory.objects.all()
        authentication = SessionAuthentication()
        authorization = AuthorizationWithObjectPermissions()


class JobSelectedSubCategoryResource(ModelResource):
    job = fields.ToOneField('employer.api.JobResource', 'job')
    subcategory = fields.ToOneField(JobSubCategoryResource, 'sub_category')

    def lookup_kwargs_with_identifiers(self, bundle, kwargs):
        lookup_kwargs = super(JobSelectedSubCategoryResource, self).lookup_kwargs_with_identifiers(bundle,kwargs)
        if lookup_kwargs == {}:
            return {'pk': -1}
        return lookup_kwargs

    class Meta:
        queryset = JobSelectedSubCategory.objects.all()
        authentication = SessionAuthentication()
        authorization = AuthorizationWithObjectPermissions()
