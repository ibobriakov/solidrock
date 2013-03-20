from django.contrib.auth import logout
from django.http.response import HttpResponseRedirect

__author__ = 'ir4y'


def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/")
