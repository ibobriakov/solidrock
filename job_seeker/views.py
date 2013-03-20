# Create your views here.
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView
from userprofile.models import JobSeeker


class JobSeekerBaseDetailView(DetailView):
    model = JobSeeker
    context_object_name = 'profile'
    template_name = 'job_seeker/detail.html'

    def get_object(self, queryset=None):
        return get_object_or_404(self.model, user=self.request.user)


class JobSeekerInformationDetailView(DetailView):
    model = JobSeeker
    template_name = 'job_seeker/information_detail.html'

    def get_object(self, queryset=None):
        return get_object_or_404(self.model, user=self.request.user)