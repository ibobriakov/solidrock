# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from tastypie.api import Api
from cover_letter.api import CoverLetterResource, CoverLetterItemResource
from payment.api import SubscriptionTypeResource, AdPackageTypeResource, AdPackageResource, SubscriptionResource
from registration_rest_backend.api import JobSeekerRegistrationResource, EmployerRegistrationResource,\
    ActivationResource, LoginResource
from resume.api import ResumeItemResource, ResumeResource
from userprofile.api import JobSeekerInformationResource, JobSeekerCurrentEmploymentResource,\
    JobSeekerPreviousEmploymentResource, JobSeekerEducationResource, JobSeekerRefereeResource, \
    EmployerResource
from employer.api import JobResource, LocationResource, HourResource,\
    EmploymentTypeResource, SpecialConditionResource, EssentialResource, DesireableResource,\
    JobCategoryResource, JobSubCategoryResource, JobUploadDocumentResource,\
    JobUploadDocumentTypeResource, JobSelectedCategoryResource, JobSelectedSubCategoryResource,\
    JobExecutivePositionsResource,JobAreaResource
from contactus.api import FeedbackResource
from job_seeker.api import ApplyToJobResource

v1_api = Api(api_name='v1')
v1_api.register(EmployerResource())
v1_api.register(CoverLetterResource())
v1_api.register(CoverLetterItemResource())
v1_api.register(ResumeResource())
v1_api.register(ResumeItemResource())
v1_api.register(JobSeekerRegistrationResource())
v1_api.register(EmployerRegistrationResource())
v1_api.register(JobSeekerInformationResource())
v1_api.register(JobSeekerCurrentEmploymentResource())
v1_api.register(JobSeekerPreviousEmploymentResource())
v1_api.register(JobSeekerEducationResource())
v1_api.register(JobSeekerRefereeResource())
v1_api.register(ActivationResource())
v1_api.register(LoginResource())
v1_api.register(JobResource())
v1_api.register(JobAreaResource())
v1_api.register(LocationResource())
v1_api.register(HourResource())
v1_api.register(EmploymentTypeResource())
v1_api.register(SpecialConditionResource())
v1_api.register(EssentialResource())
v1_api.register(DesireableResource())
v1_api.register(JobCategoryResource())
v1_api.register(JobSubCategoryResource())
v1_api.register(JobUploadDocumentTypeResource())
v1_api.register(JobUploadDocumentResource())
v1_api.register(JobSelectedCategoryResource())
v1_api.register(JobSelectedSubCategoryResource())
v1_api.register(JobExecutivePositionsResource())
v1_api.register(FeedbackResource())
v1_api.register(SubscriptionTypeResource())
v1_api.register(AdPackageTypeResource())
v1_api.register(AdPackageResource())
v1_api.register(SubscriptionResource())

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
    url(r'^', include('main.urls')),
)

urlpatterns += patterns('django.contrib.flatpages.views',
                        url(r'^explore/$', 'flatpage', {'url': '/explore/'}, name='explore'),
                        url(r'^contact_us/$', 'flatpage', {'url': '/contact_us/'}, name='contact_us'),
                        url(r'^job_seekers/$', 'flatpage', {'url': '/job_seekers/'}, name='job_seekers'),
                        )

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += patterns('django.contrib.flatpages.views',
                        (r'^(?P<url>.*)$', 'flatpage'),
                        )
