from django.views.generic import TemplateView

__author__ = 'jackdevil'


class MainRegistration(TemplateView):
    template_name = 'registration/main.html'