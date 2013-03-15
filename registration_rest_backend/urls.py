# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from views import MainRegistration

__author__ = 'jackdevil'

urlpatterns = patterns(
    '',
    url(r'^$', MainRegistration.as_view()),
)
