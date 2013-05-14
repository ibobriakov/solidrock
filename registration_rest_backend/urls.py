from django.conf.urls import patterns
from django.conf.urls import url
from django.contrib.auth import views as auth_views

__author__ = 'ir4y'

urlpatterns = patterns('',
                       url(r'^change/$',
                           auth_views.password_change,
                           name='auth_password_change'),
                       url(r'^change/done/$',
                           auth_views.password_change_done,
                           name='auth_password_change_done'),
                       url(r'^reset/$',
                           auth_views.password_reset,
                           name='auth_password_reset'),
                       url(r'^reset/confirm/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$',
                           auth_views.password_reset_confirm,
                           name='auth_password_reset_confirm'),
                       url(r'^reset/complete/$',
                           auth_views.password_reset_complete,
                           name='auth_password_reset_complete'),
                       url(r'^reset/done/$',
                           auth_views.password_reset_done,
                           name='auth_password_reset_done'),
                       )