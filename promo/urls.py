# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from views import EmployersPromo


urlpatterns = patterns(
    '',
    url(r'^employers/$', EmployersPromo.as_view(), name='promo.employers'),
)
