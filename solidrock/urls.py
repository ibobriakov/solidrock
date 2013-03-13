# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from tastypie.api import Api
from cover_letter.api import CoverLetterItemResource
from registration_rest_backend.api import RegistrationResource, ActivationResource
from resume.api import ResumeItemResource

v1_api = Api(api_name='v1')
v1_api.register(CoverLetterItemResource())
v1_api.register(ResumeItemResource())
v1_api.register(RegistrationResource())
v1_api.register(ActivationResource())


admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^registration/', include('registration_rest_backend.urls')),
    url(r'^cover_letter/', include('cover_letter.urls')),
    url(r'^resume/', include('resume.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(v1_api.urls)),
    url(r'^', include('main.urls')),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
