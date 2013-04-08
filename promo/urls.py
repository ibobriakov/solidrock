# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from views import EmployersPromo


urlpatterns = patterns(
    '',
    url(r'^employers/$', EmployersPromo.as_view(), name='promo.employers'),
    url(r'^coming_soon/$', TemplateView.as_view(template_name="landing/comming_soon.html"), name='promo.coming_soon'),
)
