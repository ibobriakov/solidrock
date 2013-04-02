# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from views import SearchView


__author__ = 'ir4y'

urlpatterns = patterns(
    '',
    url(r'^$', SearchView.as_view(), name='search.search'),)
