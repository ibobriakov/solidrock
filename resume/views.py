from django.core.urlresolvers import reverse
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import DetailView
from models import Resume


def create_resume_view(request):
    new_resume = Resume.objects.create(owner=request.user, name="New Resume")
    return HttpResponseRedirect(reverse('resume.edit', args=[new_resume.pk]))


class ResumeView(DetailView):
    template_name = 'resume/main.html'
    model = Resume

    def get_object(self, queryset=None):
        object = super(ResumeView, self).get_object(queryset)
        if object.owner != self.request.user:
            raise Http404
        return  object


def delete_resume_view(request, resume_pk):
    get_object_or_404(Resume, pk=resume_pk, owner=request.user).delete()
    return redirect('job_seeker.profile.base')