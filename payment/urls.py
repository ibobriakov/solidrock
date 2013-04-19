# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from views import PaymentView, PricingView

__author__ = 'ir4y'

urlpatterns = patterns('',
                       url(r'^$', PaymentView.as_view(), name='payment'),
                       url(r'^pricing/$', PricingView.as_view(), name='pricing'),
)