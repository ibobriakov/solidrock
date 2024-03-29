# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from django.utils.decorators import method_decorator
from django.views.generic import DetailView
from userprofile.models import JobSeeker
from models import ApplyToJob


class JobSeekerBaseDetailView(DetailView):
    model = JobSeeker
    context_object_name = 'profile'
    template_name = 'job_seeker/main.html'

    def get_object(self, queryset=None):
        return get_object_or_404(self.model, user=self.request.user)

    @method_decorator(login_required(login_url='/#login'))
    def dispatch(self, request, *args, **kwargs):
        return super(JobSeekerBaseDetailView, self).dispatch(request, *args, **kwargs)


class JobSeekerInformationDetailView(DetailView):
    model = JobSeeker
    template_name = 'job_seeker/profile/edit.html'
    context_object_name = 'profile'

    def get_object(self, queryset=None):
        return get_object_or_404(self.model, user=self.request.user)

    @method_decorator(login_required(login_url='/#login'))
    def dispatch(self, request, *args, **kwargs):
        return super(JobSeekerInformationDetailView, self).dispatch(request, *args, **kwargs)


class JobSeekerInformationPublicView(DetailView):
    model = JobSeeker
    template_name = 'job_seeker/profile/view.html'


def apply_for(request, job_id):
    #todo reafctor over rest api
    ApplyToJob.objects.create(job_seeker=request.user, job_id=job_id)
    return redirect("/")
