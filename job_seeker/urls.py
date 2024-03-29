# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from views import JobSeekerBaseDetailView, JobSeekerInformationDetailView, JobSeekerInformationPublicView, apply_for


urlpatterns = patterns(
    '',
    url(r'^$', JobSeekerBaseDetailView.as_view(), name='job_seeker.profile.base'),
    url(r'^information/$', JobSeekerInformationDetailView.as_view(), name='job_seeker.profile.information'),
    url(r'^(?P<pk>\d+)/$', JobSeekerInformationPublicView.as_view(), name='job_seeker.profile.information.public'),
    url(r'^apply_for/(?P<job_id>\d+)$', apply_for, name='job_seeker.apply_for'), )
