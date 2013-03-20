from django.core.urlresolvers import reverse
from django.http import Http404, HttpResponseRedirect
from django.views.generic import DetailView, DeleteView
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


class ResumeDeleteView(DeleteView):
    def get_success_url(self):
        return self.request.user.profile.url