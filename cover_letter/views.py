# Create your views here.
from django.views.generic import TemplateView


class CoverLetterView(TemplateView):
    template_name = 'cover_letter/main.html'
