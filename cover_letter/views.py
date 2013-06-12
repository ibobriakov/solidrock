from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import redirect, get_object_or_404
from django.utils.decorators import method_decorator
from django.views.generic import DetailView
from dynamic_paper.views import PdfRenderMixin
from employer.models import Job
from models import CoverLetter
from forms import CoverLetterSelectForm


@login_required(login_url='/#login')
def create_cover_letter_view(request):
    new_cover_letter = CoverLetter.objects.create(owner=request.user, name="Cover Letter")
    if 'job' in request.GET:
        request.session['autocreate_cover_letter'] = {'job': request.GET['job'], 'cover_letter': new_cover_letter.pk}
    return redirect('cover_letter.edit', new_cover_letter.pk)


class CoverLetterView(DetailView):
    template_name = 'cover_letter/edit.html'
    model = CoverLetter
    context_object_name = 'cover_letter'

    def get_object(self, queryset=None):
        object = super(CoverLetterView, self).get_object(queryset)
        if object.owner != self.request.user:
            raise Http404
        return object

    def get_context_data(self, **kwargs):
        context = super(CoverLetterView, self).get_context_data(**kwargs)
        context['selected'] = CoverLetter.objects.filter(owner=self.request.user).exclude(pk=self.object.pk)
        if 'autocreate_cover_letter' in self.request.session:
            if context['object'].pk == self.request.session['autocreate_cover_letter']['cover_letter']:
                try:
                    context['for_job'] = Job.objects.get(pk=self.request.session['autocreate_cover_letter']['job'])
                except Job.DoesNotExist:
                    pass
        return context

    @method_decorator(login_required(login_url='/#login'))
    def dispatch(self, request, *args, **kwargs):
        return super(CoverLetterView, self).dispatch(request, *args, **kwargs)


class CoverLetterViewPublic(DetailView):
    template_name = 'cover_letter/view.html'
    model = CoverLetter
    context_object_name = 'cover_letter'


class CoverLetterPDFView(PdfRenderMixin, DetailView):
    template_name = 'cover_letter/pdf.html'
    model = CoverLetter


@login_required(login_url='/#login')
def delete_cover_letter_view(request, resume_pk):
    get_object_or_404(CoverLetter, pk=resume_pk, owner=request.user).delete()
    return redirect('job_seeker.profile.base')