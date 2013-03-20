# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from views import JobSeekerBaseDetailView, JobSeekerInformationDetailView


urlpatterns = patterns(
    '',
    url(r'^$',
        JobSeekerBaseDetailView.as_view(),
        name='job_seeker.profile.base'),
    url(r'^information/$',
        JobSeekerInformationDetailView.as_view(),
        name='job_seeker.profile.information'),
    )
