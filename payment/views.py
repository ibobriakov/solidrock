from django.views.generic import FormView
from forms import PaymentForm
from egate import process, CheckoutError


class PaymentView(FormView):
    template_name = "payment_form.html"
    form_class = PaymentForm

    def form_valid(self, form):
        context = self.get_context_data(form=form)
        try:
            context['result'] = process(self.request, self.request.POST['amount'])
        except CheckoutError as err:
            context['result'] = err

        return self.render_to_response(context)
