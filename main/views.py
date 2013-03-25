# -*- coding: utf-8 -*-
import json
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from sorl.thumbnail.shortcuts import get_thumbnail


class MainView(TemplateView):
    template_name = 'main.html'


@csrf_exempt
def upload(request, purpose):
    if purpose == 'job_seeker_photo':
        job_seeker_information = request.user.profile.personal_information
        job_seeker_information.photo = request.FILES['files[]']
        job_seeker_information.save()
        url = get_thumbnail(job_seeker_information.photo, '203x203', crop="center").url
    return HttpResponse(json.dumps({'url': url}), mimetype='application/json')


def url_resolver(request):
    #todo add caching
    javascript_code = "var url_resolver=" + json.dumps({
        'cover_letter': reverse('api_dispatch_list', kwargs={'api_name': 'v1', 'resource_name': 'cover_letter'}),
        'resume': reverse('api_dispatch_list', kwargs={'api_name': 'v1', 'resource_name': 'resume'}),
    }) + ";"
    return HttpResponse(javascript_code, mimetype='text/javascript')
