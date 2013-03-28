from django.http import Http404
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import DetailView, TemplateView
from models import Job


class EmployerView(TemplateView):
    template_name = "employer/detail.html"


def create_job_view(request):
    new_job = Job.objects.create(owner=request.user,
                                 contact_phone=request.user.profile.business_phone,
                                 contact_email=request.user.profile.email)
    return redirect('employer.job.edit', new_job.pk)


class EditJobView(DetailView):
    template_name = "employer/main.html"
    model = Job

    def get_object(self, queryset=None):
        object = super(EditJobView, self).get_object(queryset)
        if object.owner != self.request.user:
            raise Http404
        return  object


def delete_job_view(request, pk):
    get_object_or_404(Job, pk=pk, owner=request.user).delete()
    return redirect('employer.profile.base')