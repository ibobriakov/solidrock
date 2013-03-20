# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from cover_letter.views import create_cover_letter_view, CoverLetterView, delete_cover_letter_view

__author__ = 'jackdevil'

urlpatterns = patterns(
    '',
    url(r'^create/$', create_cover_letter_view, name='cover_letter.create'),
    url(r'^(?P<pk>\d+)/$', CoverLetterView.as_view(), name='cover_letter.edit'),
    url(r'^(?P<resume_pk>\d+)/delete$', delete_cover_letter_view, name='cover_letter.delete'),
)
