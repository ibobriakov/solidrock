# -*- coding: utf-8 -*-
import json
from constance import config
from django.core.urlresolvers import reverse
from django.http import HttpResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView, ListView
from sorl.thumbnail.shortcuts import get_thumbnail
from employer.models import JobUploadDocument, JobUploadDocumentType
from search.forms import SearchForm
from userprofile.models import Employer


class MainView(TemplateView):
    template_name = 'main.html'

    def get_context_data(self, **kwargs):
        context = super(MainView, self).get_context_data(**kwargs)
        context['next'] = self.request.GET['next'] if 'next' in self.request.GET else None
        context['search_from'] = SearchForm()
        return context


class EmployerListView(ListView):
    template_name = 'employers.html'
    model = Employer


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
    elif purpose == 'job_support_document':
        document_type = JobUploadDocumentType.objects.get(name="Support Document")
        upload_document = JobUploadDocument()
        upload_document.job_id = pk
        upload_document.document_type_id = document_type.pk
        upload_document.document = request.FILES['files[]']
        upload_document.save()
        return reverse('api_dispatch_detail', api_name='v1', resource_name='job_upload_document', pk=upload_document.pk)
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
    else:
        raise Http404
    return HttpResponse(json.dumps({'url': url}), mimetype='application/json')