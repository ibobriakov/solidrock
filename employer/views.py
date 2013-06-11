import datetime
from functools import wraps
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.urlresolvers import reverse
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect
from django.utils.decorators import available_attrs
from django.views.generic import DetailView, TemplateView, ListView
from django.views.generic.list import MultipleObjectMixin
from job_seeker.forms import ApplyToJobForm
from job_seeker.models import ApplyToJob
from main.utils import view_decorator
from models import Job
from payment.models import SubscriptionType, AdPackageType, Subscription, AdPackage
from resume.models import Resume
from userprofile.models import Employer
from employer.forms import JobForm


def profile_complete(view_func):
    @wraps(view_func, assigned=available_attrs(view_func))
    def _wrapped_view(request, *args, **kwargs):
        if request.user.profile.complete:
            return view_func(request, *args, **kwargs)
        else:
            return redirect('employer.profile.edit')
    return _wrapped_view


@view_decorator(login_required(login_url='/#login'))
@view_decorator(profile_complete)
class EmployerView(DetailView):
    model = Employer
    context_object_name = 'profile'
    template_name = "employer/main.html"

    def get_object(self, queryset=None):
        return get_object_or_404(self.model, user=self.request.user)


class EmployerEditView(TemplateView):
    template_name = "employer/detail.html"


@profile_complete
def create_job_view(request):
    new_job = Job.objects.create(owner=request.user,
                                 open_date=datetime.datetime.now().date(),
                                 contact_name=request.user.profile.name,
                                 contact_phone=request.user.profile.business_phone,
                                 contact_email=request.user.profile.email)
    return redirect('employer.job.edit', new_job.pk)


@view_decorator(profile_complete)
class JobListView(ListView):
    template_name = "employer/job_list.html"
    model = Job

    def get_queryset(self):
        return super(JobListView, self).get_queryset().filter(owner=self.request.user)


@view_decorator(profile_complete)
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
            context['user_subscription'] = Subscription.objects.filter(owner=self.request.user,
                                                                       finish_date__gte=datetime.datetime.now())[0]
        except IndexError:
            context['user_subscription'] = False
        try:
            context['user_package'] = AdPackage.objects.filter(owner=self.request.user).exclude(count=0)[0]
        except IndexError:
            context['user_package'] = False

        return context


@profile_complete
def delete_job_view(request, pk):
    get_object_or_404(Job, pk=pk, owner=request.user).delete()
    return redirect('employer.profile.base')


class JobPublicView(DetailView):
    template_name = "employer/public_job.html"
    model = Job

    def get_context_data(self, **kwargs):
        context = super(JobPublicView, self).get_context_data(**kwargs)
        if not self.request.user.is_anonymous():
            try:
                form = ApplyToJobForm(instance=self.request.user.applytojob_set.get(job=self.object))
                context['already_applied'] = True
            except ApplyToJob.DoesNotExist:
                initial = {'job': self.object.pk}
                if 'autocreate_resume' in self.request.session:
                    if int(self.request.session['autocreate_resume']['job']) == context['object'].pk:
                        resume_pk = self.request.session['autocreate_resume']['resume']
                        initial['resume'] = reverse('api_dispatch_detail',
                                                    kwargs={'api_name': 'v1',
                                                            'resource_name': 'resume_name',
                                                            'pk': resume_pk})
                if 'autocreate_cover_letter' in self.request.session:
                    if int(self.request.session['autocreate_cover_letter']['job']) == context['object'].pk:
                        cover_letter_pk = self.request.session['autocreate_cover_letter']['cover_letter']
                        initial['cover_letter'] = reverse('api_dispatch_detail',
                                                                     kwargs={'api_name': 'v1',
                                                                             'resource_name': 'cover_letter_name',
                                                                             'pk': cover_letter_pk})

                form = ApplyToJobForm(initial=initial)
                context['already_applied'] = False
            form.fields['resume'].queryset = self.request.user.resume_set.all()
            form.fields['cover_letter'].queryset = self.request.user.coverletter_set.all()
            context['apply_job_form'] = form
        return context


@view_decorator(profile_complete)
class EmployerPublicView(DetailView, MultipleObjectMixin):
    template_name = "employer/public.html"
    model = Employer
    paginate_by = 9

    def get_context_data(self, **kwargs):
        kwargs['object_list'] = self.object.user.job_set.approved()
        return super(EmployerPublicView, self).get_context_data(**kwargs)