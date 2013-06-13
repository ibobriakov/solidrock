from django.forms.models import modelform_factory
from tastypie import fields
from tastypie.authentication import SessionAuthentication
from tastypie.resources import ModelResource
from main.api import AuthorizationWithObjectPermissions
from ..models import ApplyToJob
from validation import ApplyToJobValidation


__author__ = 'ir4y'


class ApplyToJobResource(ModelResource):
    resume = fields.ToOneField('resume.api.ResumeResource', 'resume', blank=True, null=True)
    cover_letter = fields.ToOneField('cover_letter.api.CoverLetterResource', 'cover_letter', blank=True, null=True)

    def hydrate(self, bundle):
        bundle.obj.job_seeker = bundle.request.user
        bundle.obj.job_id = bundle.data['job']
        for item in ('cover_letter', 'resume',):
            if bundle.data[item] == '':
                del(bundle.data[item])
        return bundle

    class Meta:
        queryset = ApplyToJob.objects.all()
        authentication = SessionAuthentication()
        authorization = AuthorizationWithObjectPermissions()
        validation = ApplyToJobValidation(form_class=modelform_factory(ApplyToJob))