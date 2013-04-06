# -*- coding: utf-8 -*-
import json
from constance import config
from django.http import HttpResponse, Http404
from django.shortcuts import redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView, ListView
from sorl.thumbnail.shortcuts import get_thumbnail
from employer.models import JobUploadDocument, JobUploadDocumentType, Job
from search.forms import SearchForm
from userprofile.models import Employer


class MainView(TemplateView):
    template_name = 'main.html'

    def get_context_data(self, **kwargs):
        context = super(MainView, self).get_context_data(**kwargs)
        context['next'] = self.request.GET['next'] if 'next' in self.request.GET else None
        context['search_from'] = SearchForm()
        context['featured_jobs'] = Job.objects.filter(featured_job=True)
        return context


class EmployerListView(ListView):
    template_name = 'employers.html'
    model = Employer


def get_document_type(type_slug):
    def get_support_document_type():
        try:
            return JobUploadDocumentType.objects.get(name="Support Document")
        except JobUploadDocumentType.DoesNotExist:
            raise Exception("Did you setup 'employer/fixtures/document_type.json' fictures ?")

    def get_full_position_document_type():
        try:
            return JobUploadDocumentType.objects.get(name="Full Position Description")
        except JobUploadDocumentType.DoesNotExist:
            raise Exception("Did you setup 'employer/fixtures/document_type.json' fictures ?")
    return {'job_support_document': get_support_document_type,
            'job_full_position_document': get_full_position_document_type}[type_slug]()

@csrf_exempt
def upload(request, purpose, pk=None):
    if purpose == 'job_seeker_photo':
        job_seeker_information = request.user.profile.personal_information
        job_seeker_information.photo = request.FILES['files[]']
        job_seeker_information.save()
        url = get_thumbnail(job_seeker_information.photo, '203x203', crop="center").url
    elif purpose == 'employer_company_logo':
        employer_profile = request.user.profile
        employer_profile.logo = request.FILES['files[]']
        employer_profile.save()
        url = get_thumbnail(employer_profile.logo, '203x203', crop="center").url
    elif purpose in ('job_support_document', 'job_full_position_document'):
        job = get_object_or_404(Job, pk=pk, owner=request.user)
        upload_document = JobUploadDocument()
        upload_document.job = job
        upload_document.document_type = get_document_type(purpose)
        upload_document.document = request.FILES['files[]']
        upload_document.save()
        return redirect('api_dispatch_detail', 'v1', 'job_upload_document', upload_document.pk)
    else:
        raise Http404
    return HttpResponse(json.dumps({'url': url}), mimetype='application/json')


@csrf_exempt
def remove(request, purpose, pk=None):
    if purpose == 'job_seeker_photo':
        job_seeker_information = request.user.profile.personal_information
        job_seeker_information.photo = None
        job_seeker_information.save()
        url = config.DEFAULT_AVATAR
    elif purpose == 'employer_company_logo':
        employer_profile = request.user.profile
        employer_profile.logo = None
        employer_profile.save()
        url = config.DEFAULT_COMPANY_LOGO
    elif purpose in ('job_support_document', 'job_full_position_document'):
        get_object_or_404(JobUploadDocumentType,
                          type=get_document_type(purpose),
                          job__owner=request.user,
                          pk=pk).delete()
        url = False
    else:
        raise Http404
    return HttpResponse(json.dumps({'url': url}), mimetype='application/json')