from django.views.generic import TemplateView
from forms import FeedbackForm


class ContactUsView(TemplateView):
    template_name = "contactus/contactus.html"

    def get_context_data(self, **kwargs):
        context = super(ContactUsView, self).get_context_data(**kwargs)
        context['form'] = FeedbackForm()
        return context