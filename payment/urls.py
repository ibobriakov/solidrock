# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from views import PaymentView, PricingView

__author__ = 'ir4y'

urlpatterns = patterns('payment.views',
                       url(r'^$', PaymentView.as_view(), name='payment'),
                       url(r'^pay_redirect/$','pay_redirect', name='pay_redirect'),
                       url(r'^pay_callback$','pay_callback', name='pay_callback'),
                       url(r'^pricing/$', PricingView.as_view(), name='pricing'),
)