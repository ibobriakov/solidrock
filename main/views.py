# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.views.generic import TemplateView


class MainView(TemplateView):
    template_name = 'base.html'


def url_resolver(request):
    return HttpResponse('',mimetype='text/javascript')