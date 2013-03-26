# -*- coding: utf-8 -*-
import json
from constance import config
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from sorl.thumbnail.shortcuts import get_thumbnail


class MainView(TemplateView):
    template_name = 'main.html'

    def get_context_data(self, **kwargs):
        context = super(MainView, self).get_context_data(**kwargs)
        context['next'] = self.request.GET['next'] if 'next' in self.request.GET else None
        return context


@csrf_exempt
def upload(request, purpose):
    if purpose == 'job_seeker_photo':
        job_seeker_information = request.user.profile.personal_information
        job_seeker_information.photo = request.FILES['files[]']
        job_seeker_information.save()
        url = get_thumbnail(job_seeker_information.photo, '203x203', crop="center").url
    return HttpResponse(json.dumps({'url': url}), mimetype='application/json')


@csrf_exempt
def remove(request, purpose):
    if purpose == 'job_seeker_photo':
        job_seeker_information = request.user.profile.personal_information
        job_seeker_information.photo = None
        job_seeker_information.save()
        url = config.DEFAULT_AVATAR
    return HttpResponse(json.dumps({'url': url}), mimetype='application/json')