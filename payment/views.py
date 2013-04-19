from django.views.generic import FormView
from forms import PaymentForm
from tasks import process_payment


class PaymentView(FormView):
    template_name = "payment_form.html"
    form_class = PaymentForm

    def form_valid(self, form):
        context = self.get_context_data(form=form)
        process_payment.delay(self.request.user,
                              form.data['amount'].strip(),
                              form.data['card_number'].strip(),
                              form.data['card_expiry_year'][2:].strip() +
                              form.data['card_expiry_month'].strip(),
                              form.data['card_ccv'].strip())
        context['result'] = 'Your payment in process'
        return self.render_to_response(context)
