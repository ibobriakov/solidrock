import copy
from hashlib import md5
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views.generic import FormView, TemplateView
from django.conf import settings
from forms import PaymentForm
from models import AdPackageType, SubscriptionType, Transaction
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


class PricingView(TemplateView):
    template_name = "pricing.html"

    def get_context_data(self, **custom_contex):
        custom_contex['subscriptions'] = SubscriptionType.objects.all()
        custom_contex['packages'] = AdPackageType.objects.exclude(default=True)
        custom_contex['default'] = AdPackageType.objects.get(default=True)
        return super(PricingView, self).get_context_data(**custom_contex)


def pay_redirect(request):
    secure_secret = copy.copy(settings.SECURE_SECRET)
    transaction = Transaction.objects.create(owner=request.user,
                                             amount=request.GET['amount'])
    POST_DATA = {
        'vpc_Version': '1',
        'vpc_Command': 'pay',
        'vpc_AccessCode': '9F3486FE',
        'vpc_MerchTxnRef': '{0}'.format(transaction.id),
        'vpc_Merchant': 'TESTSOLROCCOM01',
        'vpc_OrderInfo': 'VPC Example',
        'vpc_Amount': request.GET['amount'],
        'vpc_ReturnURL': 'http://localhost:8000'+reverse('pay_callback'),
        'vpc_Locale': 'en',
    }
    for key in sorted(POST_DATA.keys()):
        secure_secret += POST_DATA[key]
    POST_DATA['vpc_SecureHash'] = md5(secure_secret).hexdigest().upper()
    tail = "&".join(["%s=%s" % (key, value) for key, value in POST_DATA.iteritems()])
    return HttpResponseRedirect("https://migs.mastercard.com.au/vpcpay?"+tail)


def pay_callback(request):
    #todo check secure hash
    transaction = get_object_or_404(Transaction, pk=request.GET['vpc_MerchTxnRef'])
    response_code = request.GET.get('vpc_TxnResponseCode', "9999")
    if response_code != '0':
        transaction.error_code = int(response_code)
        transaction.error = request.GET.get("vpc_Message", 'Unknown error')
    else:
        transaction.approved = True
        transaction.result = int(request.GET["vpc_TransactionNo"])
    transaction.save()
    return HttpResponseRedirect("/")

