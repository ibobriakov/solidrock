from celery import task
from egate import process, CheckoutError
from models import Transaction
__author__ = 'ir4y'


@task
def process_payment(user, amount, card_number, card_exp, card_sec_code):
    transaction = Transaction.objects.create(owner=user,
                                             amount=amount)
    order = "order:{0}".format(transaction.pk)
    try:
        result = process(amount, card_number, card_exp, card_sec_code,order_info=order, merch_ref=order)
        if result["vpc_TxnResponseCode"] != "0":
            transaction.error_code = int(result["vpc_TxnResponseCode"])
            transaction.error = result["vpc_Message"]
        else:
            transaction.approved = True
            transaction.result = int(result["vpc_TransactionNo"])
        transaction.save()
    except CheckoutError as err:
        transaction.error = str(err)
        transaction.save()
    return transaction
