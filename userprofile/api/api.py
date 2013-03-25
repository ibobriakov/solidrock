from django.forms.models import modelform_factory
from sorl.thumbnail.shortcuts import get_thumbnail
from tastypie import fields
from tastypie.authentication import SessionAuthentication
from tastypie.exceptions import ImmediateHttpResponse
from tastypie.resources import ModelResource
from tastypie.validation import FormValidation
from constance import config
from main.api import ResourceFieldsOrderSchemaMixin, ResourceLabelSchemaMixin, ResourceTypesOverrideSchemaMixin
from ..models import JobSeekerInformation, JobSeekerCurrentEmployment, JobSeekerPreviousEmployment,\
    JobSeekerEducation, JobSeekerReferee, Employer, JobSeekerEducationType
from main.api.authorization import AuthorizationWithObjectPermissions


__author__ = 'ir4y'


class EmployerResource(ResourceLabelSchemaMixin, ResourceFieldsOrderSchemaMixin, ModelResource):
    def get_object_list(self, request):
        query_set = super(EmployerResource, self).get_object_list(request)
        return query_set.filter(user=request.user)

    def hydrate(self, bundle):
        bundle.obj.user = bundle.request.user
        return bundle

    class Meta:
        queryset = Employer.objects.all()
        resource_name = 'employer'
        always_return_data = True
        authentication = SessionAuthentication()
        authorization = AuthorizationWithObjectPermissions()
        validation = FormValidation(form_class=modelform_factory(Employer))


class JobSeekerItemResource(ResourceLabelSchemaMixin, ResourceFieldsOrderSchemaMixin, ModelResource):
    def get_object_list(self, request):
        query_set = super(JobSeekerItemResource, self).get_object_list(request)
        return query_set.filter(job_seeker=request.user.profile)

    def hydrate(self, bundle):
        bundle.obj.job_seeker = bundle.request.user.profile
        return bundle


class JobSeekerInformationResource(JobSeekerItemResource):
    first_name = fields.CharField()
    last_name = fields.CharField()
    photo = fields.FileField(readonly=True)

    def dehydrate_have_visa(self, bundle):
        return str(bundle.obj.have_visa).lower()

    def dehydrate_is_australian(self, bundle):
        return str(bundle.obj.is_australian).lower()

    def dehydrate_is_driver(self, bundle):
        return str(bundle.obj.is_driver).lower()

    def dehydrate_can_contact_at_work(self, bundle):
        return str(bundle.obj.can_contact_at_work).lower()

    def dehydrate_first_name(self, bundle):
        return bundle.obj.job_seeker.user.first_name

    def dehydrate_last_name(self, bundle):
        return bundle.obj.job_seeker.user.last_name

    def dehydrate_photo(self, bundle):
        if bundle.obj.photo:
            return get_thumbnail(bundle.obj.photo, '203x203', crop="center").url
        else:
            return config.DEFAULT_AVATAR

    def hydrate(self, bundle):
        super(JobSeekerInformationResource, self).hydrate(bundle)
        bundle.obj.job_seeker.user.first_name = bundle.data['first_name']
        bundle.obj.job_seeker.user.last_name = bundle.data['last_name']
        return bundle

    def save(self, bundle, skip_errors=False):
        user_update = bundle.obj.job_seeker.user
        # self.is_valid(bundle) clash bundle.obj.job_seeker.user
        self.is_valid(bundle)

        if bundle.errors and not skip_errors:
            raise ImmediateHttpResponse(response=self.error_response(bundle.request, bundle.errors))

        user_update.save()
        return super(JobSeekerInformationResource, self).save(bundle,skip_errors)

    class Meta:
        queryset = JobSeekerInformation.objects.all()
        resource_name = 'job_seeker_information'
        always_return_data = True
        authentication = SessionAuthentication()
        authorization = AuthorizationWithObjectPermissions()
        validation = FormValidation(form_class=modelform_factory(JobSeekerInformation))


class JobSeekerCurrentEmploymentResource(JobSeekerItemResource):
    class Meta:
        queryset = JobSeekerCurrentEmployment.objects.all()
        resource_name = 'job_seeker_current_employment'
        always_return_data = True
        authentication = SessionAuthentication()
        authorization = AuthorizationWithObjectPermissions()
        validation = FormValidation(form_class=modelform_factory(JobSeekerCurrentEmployment))


class JobSeekerPreviousEmploymentResource(JobSeekerItemResource):
    class Meta:
        queryset = JobSeekerPreviousEmployment.objects.all()
        resource_name = 'job_seeker_previous_employment'
        always_return_data = True
        authentication = SessionAuthentication()
        authorization = AuthorizationWithObjectPermissions()
        validation = FormValidation(form_class=modelform_factory(JobSeekerPreviousEmployment))


class JobSeekerEducationResource(JobSeekerItemResource):
    education_type = fields.CharField('education_type_id')

    def dehydrate_education_type(self, bundle):
        return bundle.obj.education_type.type_name_slug

    def hydrate_education_type(self, bundle):
        education_type = JobSeekerEducationType.objects.get(type_name_slug=bundle.data['education_type'])
        bundle.data['education_type'] = education_type.pk
        return bundle

    class Meta:
        queryset = JobSeekerEducation.objects.all()
        resource_name = 'job_seeker_education'
        always_return_data = True
        authentication = SessionAuthentication()
        authorization = AuthorizationWithObjectPermissions()
        validation = FormValidation(form_class=modelform_factory(JobSeekerEducation))


class JobSeekerRefereeResource(JobSeekerItemResource):
    class Meta:
        queryset = JobSeekerReferee.objects.all()
        resource_name = 'job_seeker_referee'
        always_return_data = True
        authentication = SessionAuthentication()
        authorization = AuthorizationWithObjectPermissions()
        validation = FormValidation(form_class=modelform_factory(JobSeekerReferee))
