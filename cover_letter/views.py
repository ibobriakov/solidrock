# Create your views here.
from django.http import Http404
from django.views.generic import DetailView
from models import CoverLetter


class CoverLetterView(DetailView):
    template_name = 'cover_letter/main.html'
    model = CoverLetter

    def get_object(self, queryset=None):
        object = super(CoverLetterView, self).get_object(queryset)
        if object.owner != self.request.user:
            raise Http404
        return  object