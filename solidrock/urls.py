# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from tastypie.api import Api


def resouce_autodiscover():
    from django.conf import settings
    from django.utils.importlib import import_module
    v1_api = Api(api_name='v1')
    for app in settings.INSTALLED_APPS:
        try:
            resorce_api = import_module('%s.api' % app)
            for resource_klass_name in resorce_api.__all__:
                resource_klass = getattr(resorce_api, resource_klass_name)
                v1_api.register(resource_klass())
        except:
            continue
    return v1_api

v1_api = resouce_autodiscover()
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^job_seeker/', include('job_seeker.urls')),
    url(r'^employer/', include('employer.urls')),
    url(r'^cover_letter/', include('cover_letter.urls')),
    url(r'^resume/', include('resume.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(v1_api.urls)),
    url(r'logout/', 'registration_rest_backend.views.logout_view', name="logout"),
    url(r'^redactor/', include('redactor.urls')),
    url(r'^search/', include('search.urls')),
    url(r'^promo/', include('promo.urls')),
    url(r'^contact_us/', include('contactus.urls')),
    url(r'^payment/', include('payment.urls')),
    url(r'^password/', include('registration_rest_backend.urls')),
    url(r'^', include('main.urls')),
)

urlpatterns += patterns('django.contrib.flatpages.views',
                        url(r'^explore/$', 'flatpage', {'url': '/explore/'}, name='explore'),
                        url(r'^contact_us/$', 'flatpage', {'url': '/contact_us/'}, name='contact_us'),
                        url(r'^job_seekers/$', 'flatpage', {'url': '/job_seekers/'}, name='job_seekers'),
                        url(r'^thank_you/$', 'flatpage', {'url': '/thank_you/'}, name='thank_you'),

                        )

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns += patterns('django.contrib.flatpages.views',
#                         (r'^(?P<url>.*)$', 'flatpage'),
#                         )
