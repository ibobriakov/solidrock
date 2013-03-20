from django.http import Http404
from django.shortcuts import redirect, get_object_or_404
from django.views.generic import DetailView
from models import CoverLetter


def create_cover_letter_view(request):
    new_cover_letter = CoverLetter.objects.create(owner=request.user, name="Cover Letter")
    return redirect('cover_letter.edit', new_cover_letter.pk)


class CoverLetterView(DetailView):
    template_name = 'cover_letter/main.html'
    model = CoverLetter

    def get_object(self, queryset=None):
        object = super(CoverLetterView, self).get_object(queryset)
        if object.owner != self.request.user:
            raise Http404
        return  object


def delete_cover_letter_view(request, resume_pk):
    get_object_or_404(CoverLetter, pk=resume_pk, owner=request.user).delete()
    return redirect('job_seeker.profile.base')