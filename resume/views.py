from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect
from django.utils.decorators import method_decorator
from django.views.generic import DetailView
from dynamic_paper.views import PdfRenderMixin
from employer.models import Job
from models import Resume
from forms import ResumeSelectForm


@login_required(login_url='/#login')
def create_resume_view(request):
    new_resume = Resume.objects.create(owner=request.user, name="New Resume")
    if 'job' in request.GET:
        request.session['autocreate_resume'] = {'job': request.GET['job'], 'resume': new_resume.pk}
    return redirect('resume.edit', new_resume.pk)


class ResumeView(DetailView):
    template_name = 'resume/main.html'
    model = Resume

    def get_object(self, queryset=None):
        object = super(ResumeView, self).get_object(queryset)
        if object.owner != self.request.user:
            raise Http404
        return object

    def get_context_data(self, **kwargs):
        context = super(ResumeView, self).get_context_data(**kwargs)
        resume_select_form = ResumeSelectForm()
        resume_select_form.fields['resume'].queryset = Resume.objects.filter(owner=self.request.user)
        context['resume_select'] = resume_select_form
        if 'autocreate_resume' in self.request.session:
            if context['object'].pk == self.request.session['autocreate_resume']['resume']:
                try:
                    context['for_job'] = Job.objects.get(pk=self.request.session['autocreate_resume']['job'])
                except Job.DoesNotExist:
                    pass
        return context

    @method_decorator(login_required(login_url='/#login'))
    def dispatch(self, request, *args, **kwargs):
        return super(ResumeView, self).dispatch(request, *args, **kwargs)


class ResumePublicView(DetailView):
    template_name = 'resume/public.html'
    model = Resume


class ResumePDFView(PdfRenderMixin, DetailView):
    template_name = 'resume/pdf.html'
    model = Resume


@login_required(login_url='/#login')
def delete_resume_view(request, resume_pk):
    get_object_or_404(Resume, pk=resume_pk, owner=request.user).delete()
    return redirect('job_seeker.profile.base')