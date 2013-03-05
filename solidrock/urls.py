# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^cover_letter/', include('cover_letter.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('main.urls'))
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
