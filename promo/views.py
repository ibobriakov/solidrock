# Create your views here.
from django.views.generic import TemplateView


class EmployersPromo (TemplateView):
    template_name = 'promo/employers.html'

