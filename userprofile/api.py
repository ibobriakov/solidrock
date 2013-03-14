from tastypie import fields
from tastypie.authentication import SessionAuthentication
from tastypie.authorization import DjangoAuthorization
from tastypie.exceptions import ImmediateHttpResponse
from tastypie.resources import ModelResource
from models import JobSeekerInformation, JobSeekerCurrentEmployment, JobSeekerPreviousEmployment,\
    JobSeekerEducation, JobSeekerReferee

__author__ = 'ir4y'


class JobSeekerItemResource(ModelResource):
    def get_object_list(self, request):
        query_set = super(JobSeekerItemResource, self).get_object_list(request)
        return query_set.filter(job_seeker=request.user.profile)

    def hydrate(self, bundle):
        bundle.obj.job_seeker = bundle.request.user.profile
        return bundle


class JobSeekerInformationResource(JobSeekerItemResource):
    first_name = fields.CharField()
    last_name = fields.CharField()

    def dehydrate_first_name(self, bundle):
        return bundle.obj.job_seeker.user.first_name

    def dehydrate_last_name(self, bundle):
        return bundle.obj.job_seeker.user.last_name

    def hydrate(self, bundle):
        super(JobSeekerInformationResource, self).hydrate(bundle)
        bundle.obj.job_seeker.user.first_name = bundle.data['first_name']
        bundle.obj.job_seeker.user.last_name = bundle.data['last_name']
        return bundle

    def save(self, bundle, skip_errors=False):
        self.is_valid(bundle)

        if bundle.errors and not skip_errors:
            raise ImmediateHttpResponse(response=self.error_response(bundle.request, bundle.errors))

        bundle.obj.job_seeker.user.save()
        return super(JobSeekerInformationResource, self).save(bundle,skip_errors)

    class Meta:
        queryset = JobSeekerInformation.objects.all()
        resource_name = 'job_seeker_information'
        always_return_data = True
        authentication = SessionAuthentication()
        authorization = DjangoAuthorization()


class JobSeekerCurrentEmploymentResource(JobSeekerItemResource):
    class Meta:
        queryset = JobSeekerCurrentEmployment.objects.all()
        resource_name = 'job_seeker_current_employment'
        always_return_data = True
        authentication = SessionAuthentication()
        authorization = DjangoAuthorization()


class JobSeekerPreviousEmploymentResource(JobSeekerItemResource):
    class Meta:
        queryset = JobSeekerPreviousEmployment.objects.all()
        resource_name = 'job_seeker_previous_employment'
        always_return_data = True
        authentication = SessionAuthentication()
        authorization = DjangoAuthorization()


class JobSeekerEducationResource(JobSeekerItemResource):
    class Meta:
        queryset = JobSeekerEducation.objects.all()
        resource_name = 'job_seeker_education'
        always_return_data = True
        authentication = SessionAuthentication()
        authorization = DjangoAuthorization()


class JobSeekerRefereeResource(JobSeekerItemResource):
    class Meta:
        queryset = JobSeekerReferee.objects.all()
        resource_name = 'Job_seeker_referee'
        always_return_data = True
        authentication = SessionAuthentication()
        authorization = DjangoAuthorization()