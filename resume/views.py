from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect
from django.utils.decorators import method_decorator
from django.views.generic import DetailView
from models import Resume

@login_required(login_url='/#login')
def create_resume_view(request):
    new_resume = Resume.objects.create(owner=request.user, name="New Resume")
    return redirect('resume.edit', new_resume.pk)


class ResumeView(DetailView):
    template_name = 'resume/main.html'
    model = Resume

    def get_object(self, queryset=None):
        object = super(ResumeView, self).get_object(queryset)
        if object.owner != self.request.user:
            raise Http404
        return  object

    @method_decorator(login_required(login_url='/#login'))
    def dispatch(self, request, *args, **kwargs):
        return super(ResumeView, self).dispatch(request, *args, **kwargs)


@login_required(login_url='/#login')
def delete_resume_view(request, resume_pk):
    get_object_or_404(Resume, pk=resume_pk, owner=request.user).delete()
    return redirect('job_seeker.profile.base')