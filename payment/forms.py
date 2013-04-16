from django import forms

__author__ = 'ir4y'


class PaymentForm(forms.Form):
    amount = forms.IntegerField(initial="100")
    card_number = forms.IntegerField(initial="5123456789012346")
    card_expiry_year = forms.IntegerField(initial="2013")
    card_expiry_month = forms.IntegerField(initial="05")
    card_ccv = forms.IntegerField(initial="111")