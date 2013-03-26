from django.core.urlresolvers import resolve

__author__ = 'ir4y'


def url_name(request):
    result = {'url_name': None}
    try:
        result['url_name'] = resolve(request.get_full_path().split('?')[0]).url_name
    except:
        pass
    return result