# -*- coding: utf-8 -*-
from cover_letter.views import CoverLetterView
from django.conf.urls import patterns, url

__author__ = 'jackdevil'

urlpatterns = patterns(
    '',
    url(r'^(?P<pk>\d+)/$', CoverLetterView.as_view()),
)
