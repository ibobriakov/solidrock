# -*- coding: utf-8 -*-
import json
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.views.generic import TemplateView


class MainView(TemplateView):
    template_name = 'base.html'


def url_resolver(request):
    #todo add caching
    javascript_code = "var url_resolver=" + json.dumps({
        'cover_letter_list': reverse('api_dispatch_list', kwargs={'api_name': 'v1', 'resource_name': 'cover_letter'}),
        'resume_list': reverse('api_dispatch_list', kwargs={'api_name': 'v1', 'resource_name': 'resume'})
    }) + ";"
    return HttpResponse(javascript_code,mimetype='text/javascript')