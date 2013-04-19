from tastypie import fields
from tastypie.authentication import SessionAuthentication
from tastypie.resources import ModelResource
from main.api import AuthorizationWithObjectPermissions
from models import ApplyToJob


__author__ = 'ir4y'
__all__ = ['ApplyToJobResource']


class ApplyToJobResource(ModelResource):
    resume = fields.ToOneField('resume.ResumeResource', 'resume', blank=True, null=True)
    cover_letter = fields.ToOneField('cover_letter.CoverLetterResource', 'cover_letter', blank=True, null=True)

    def hydrate(self, bundle):
        bundle.obj.job_seeker = bundle.request.user
        bundle.obj.job_id = bundle.data['job']

    class Meta:
        queryset = ApplyToJob.objects.all()
        authentication = SessionAuthentication()
        authorization = AuthorizationWithObjectPermissions()
        # validation = JobResourceValidation(form_class=modelform_factory(Job))
