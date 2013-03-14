from tastypie.authentication import SessionAuthentication
from tastypie.authorization import DjangoAuthorization
from tastypie.resources import ModelResource
from models import JobSeekerInformation, JobSeekerCurrentEmployment, JobSeekerPreviousEmployment,\
    JobSeekerEducation, JobSeekerReferee

__author__ = 'ir4y'


class JobSeekerItemResource(ModelResource):
    def get_object_list(self, request):
        query_set = super(JobSeekerItemResource, self).get_object_list(request)
        return query_set.filter(job_seeker=request.user.profile)


class JobSeekerInformationResource(JobSeekerItemResource):
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