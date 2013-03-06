# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, include, url
from main.views import MainView


urlpatterns = patterns(
    '',
    url(r'^$', MainView.as_view(), name='main'),
    url(r'url-resolver.js', 'main.views.url_resolver', name='url-resolver')
)
