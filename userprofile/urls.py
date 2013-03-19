# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, include, url
from views import JobSeekerBaseDetailView, JobSeekerInformationDetailView


urlpatterns = patterns(
    '',
    url(r'^job_seeker/$',
        JobSeekerBaseDetailView.as_view(),
        name='job_seeker.profile.base'),
    url(r'^job_seeker/information/$',
        JobSeekerInformationDetailView.as_view(),
        name='job_seeker.profile.information'),
)
