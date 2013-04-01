# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from views import search_view


__author__ = 'ir4y'

urlpatterns = patterns(
    '',
    url(r'^search/$', search_view, name='search.search'),)
