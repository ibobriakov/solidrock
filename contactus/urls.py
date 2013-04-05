# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from views import ContactUsView

__author__ = 'jackdevil'

urlpatterns = patterns(
    '',
    url(r'^$', ContactUsView.as_view(), name='contact_us'),
    )
