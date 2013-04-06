import datetime
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import DetailView, TemplateView, ListView
from models import Job, JobLocation, Hour, EmploymentType,\
    SpecialCondition, Essential, Desireable, JobCategory, JobSubCategory, JobExecutivePositions


class EmployerView(TemplateView):
    template_name = "employer/main.html"

    def get_context_data(self, **kwargs):
        context = super(EmployerView, self).get_context_data(**kwargs)
        context['posted_jobs'] = Job.objects.filter(owner=self.request.user)
        return context


class EmployerEditView(TemplateView):
    template_name = "employer/detail.html"


def create_job_view(request):
    new_job = Job.objects.create(owner=request.user,
                                 open_date=datetime.datetime.now().date(),
                                 contact_name=request.user.profile.name,
                                 contact_phone=request.user.profile.business_phone,
                                 contact_email=request.user.profile.email)
    return redirect('employer.job.edit', new_job.pk)


class JobListView(ListView):
    template_name = "employer/job_list.html"
    model = Job

    def get_queryset(self):
        return super(JobListView, self).get_queryset().filter(owner=self.request.user)


class EditJobView(DetailView):
    template_name = "employer/post_job.html"
    model = Job

    def get_object(self, queryset=None):
        object = super(EditJobView, self).get_object(queryset)
        if object.owner != self.request.user:
            raise Http404
        return  object

    def get_context_data(self, **kwargs):
        context = super(EditJobView, self).get_context_data(**kwargs)
        context["JobLocation"] = JobLocation.objects.all()
        context["Hour"] = Hour.objects.all()
        context["EmploymentType"] = EmploymentType.objects.all()
        context["SpecialCondition"] = SpecialCondition.objects.all()
        context["Essential"] = Essential.objects.all()
        context["Desireable"] = Desireable.objects.all()
        context["JobCategory"] = JobCategory.objects.all()
        context["JobSubCategory"] = JobSubCategory.objects.all()
        context["JobExecutivePositions"] = JobExecutivePositions.objects.all()
        return context


def delete_job_view(request, pk):
    get_object_or_404(Job, pk=pk, owner=request.user).delete()
    return redirect('employer.profile.base')