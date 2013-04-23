import datetime
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect
from django.utils.decorators import method_decorator
from django.views.generic import DetailView, TemplateView, ListView
from job_seeker.forms import ApplyToJobForm
from job_seeker.models import ApplyToJob
from models import Job, JobLocation, Hour, EmploymentType,\
    SpecialCondition, Essential, Desireable, JobCategory, JobSubCategory, JobExecutivePositions
from payment.models import SubscriptionType, AdPackageType, Subscription, AdPackageHistory, AdPackage
from userprofile.models import Employer
from employer.forms import JobForm


class EmployerView(DetailView):
    model = Employer
    context_object_name = 'profile'
    template_name = "employer/main.html"

    def get_object(self, queryset=None):
        return get_object_or_404(self.model, user=self.request.user)

    @method_decorator(login_required(login_url='/#login'))
    def dispatch(self, request, *args, **kwargs):
        return super(EmployerView, self).dispatch(request, *args, **kwargs)


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
        return object

    def get_context_data(self, **kwargs):
        context = super(EditJobView, self).get_context_data(**kwargs)
        context["job_form"] = JobForm()
        context['subscriptions'] = SubscriptionType.objects.all()
        context['packages'] = AdPackageType.objects.exclude(default=True)
        context['default'] = AdPackageType.objects.get(default=True)
        try:
            context['user_subscription'] = Subscription.objects.get(owner=self.request.user)
        except Subscription.DoesNotExist:
            context['user_subscription'] = False
        try:
            context['user_package'] = AdPackage.objects.get(owner=self.request.user)
        except AdPackage.DoesNotExist:
            context['user_package'] = False
        return context


def delete_job_view(request, pk):
    get_object_or_404(Job, pk=pk, owner=request.user).delete()
    return redirect('employer.profile.base')


class JobPublicView(DetailView):
    template_name = "employer/public_job.html"
    model = Job

    def get_context_data(self, **kwargs):
        contex = super(JobPublicView, self).get_context_data(**kwargs)
        if not self.request.user.is_anonymous():
            try:
                form = ApplyToJobForm(instance=self.request.user.applytojob_set.get(job=self.object))
            except ApplyToJob.DoesNotExist:
                form = ApplyToJobForm(initial={'job': self.object})
            form.fields['resume'].queryset = self.request.user.resume_set.all()
            form.fields['cover_letter'].queryset = self.request.user.coverletter_set.all()
            contex['apply_job_form'] = form
        return contex


class EmployerPublicView(DetailView):
    template_name = "employer/public.html"
    model = Employer