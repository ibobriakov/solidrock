import copy
import json
from hashlib import md5
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, Http404, HttpResponse, HttpResponseBadRequest
from django.shortcuts import get_object_or_404
from django.views.generic import FormView, TemplateView
from django.conf import settings
from employer.models import Job
from forms import PaymentForm
from models import AdPackageType, SubscriptionType, Transaction, Order, Subscription, AdPackage
from utils import is_ads_already_paid
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
    amount = 0
    query = json.loads(request.body)
    if 'job' not in query:
        return HttpResponseBadRequest(json.dumps({'success': False, 'error': 'No job specfied'}))
    job_pk = query['job'].split('/')[-2]
    job = get_object_or_404(Job, pk=job_pk)
    amount += job.get_cost()
    ad_object = None
    if 'item' in query:
        if is_ads_already_paid(request.user):
            return HttpResponseBadRequest(json.dumps({'success': False, 'error': 'You already has ads'}))
        uri = query['item'].split('/')
        model = uri[3]
        pk = uri[4]
        if model == 'subscriptiontype':
            ad_object = get_object_or_404(SubscriptionType, pk=pk)
        elif model == 'adpackagetype':
            ad_object = get_object_or_404(AdPackageType, pk=pk)
        else:
            raise Http404
        amount += ad_object.cost
    else:
        if not is_ads_already_paid(request.user):
            return HttpResponseBadRequest(json.dumps({'success': False, 'error': 'You should buy ads'}))

    amount *= 100
    transaction = Transaction.objects.create(owner=request.user, amount=amount)
    Order.objects.create(amount=job.get_cost(),
                         transaction=transaction,
                         owner=request.user,
                         order_object=job)
    if ad_object:
        Order.objects.create(amount=ad_object.cost,
                             transaction=transaction,
                             owner=request.user,
                             order_object=ad_object)
    POST_DATA = {
        'vpc_Version': '1',
        'vpc_Command': 'pay',
        'vpc_AccessCode': '9F3486FE',
        'vpc_MerchTxnRef': '{0}'.format(transaction.id),
        'vpc_Merchant': 'TESTSOLROCCOM01',
        'vpc_OrderInfo': 'VPC Example',
        'vpc_Amount': '{0}'.format(amount),
        'vpc_ReturnURL': 'http://localhost:8000'+reverse('pay_callback'),
        'vpc_Locale': 'en',
    }
    for key in sorted(POST_DATA.keys()):
        secure_secret += POST_DATA[key]
    POST_DATA['vpc_SecureHash'] = md5(secure_secret).hexdigest().upper()
    tail = "&".join(["%s=%s" % (key, value) for key, value in POST_DATA.iteritems()])

    return HttpResponse(json.dumps({'success': True, 'redirect_url': "https://migs.mastercard.com.au/vpcpay?"+tail}))


def pay_callback(request):
    secure_secret = copy.copy(settings.SECURE_SECRET)
    for key in request.GET:
        if key != 'vpc_SecureHash':
            secure_secret += request.GET[key]
    transaction = get_object_or_404(Transaction, pk=request.GET['vpc_MerchTxnRef'])
    response_code = request.GET.get('vpc_TxnResponseCode', "9999")
    if response_code != '0':
        transaction.error_code = int(response_code)
        transaction.error = request.GET.get("vpc_Message", 'Unknown error')
    else:
        # if request.GET['vpc_SecureHash'] != md5(secure_secret).hexdigest().upper():
        #     raise Http404
        # todo fix it
        transaction.approved = True
        transaction.result = int(request.GET["vpc_TransactionNo"])
        for order in transaction.order_set.all():
            order.approved = True
            order.save()
    transaction.save()
    return HttpResponseRedirect("/")

