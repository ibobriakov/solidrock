# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from main.views import MainView, EmployerListView


urlpatterns = patterns(
    '',
    url(r'^$', MainView.as_view(), name='search'),
    url(r'^employers$', EmployerListView.as_view(), name='employers'),
    url(r'^upload/(?P<purpose>\w+)/(?P<pk>)?$', 'main.views.upload', name='upload'),
    url(r'^remove/(?P<purpose>\w+)/(?P<pk>)?$', 'main.views.remove', name='remove'),
)
