<<<<<<< HEAD
=======
import openpay
>>>>>>> 10a599bd180121a97c79de030f04398fb6a02334
from django import forms
from django.utils.translation import pgettext_lazy, ugettext_lazy as _

from ... import ChargeStatus


class OpenpayPaymentForm(forms.Form):
<<<<<<< HEAD
    first_name =
    last_name =
    card_number =
    cvc =
=======
    first_name = forms.CharField()
    last_name = forms.CharField()
    card_number = forms.CharField()
    cvc = forms.CharField()
>>>>>>> 10a599bd180121a97c79de030f04398fb6a02334
    charge_status = forms.ChoiceField(
        label=pgettext_lazy('Payment status form field', 'Payment status'),
        choices=ChargeStatus.CHOICES, initial=ChargeStatus.NOT_CHARGED,
        widget=forms.RadioSelect)

    def clean(self):
        cleaned_data = super(OpenpayPaymentForm, self).clean()

        # Partially refunded is not supported directly
        # since only last transaction of call_gateway will be processed
        charge_status = cleaned_data['charge_status']
        if charge_status in [
            ChargeStatus.PARTIALLY_CHARGED,
            ChargeStatus.PARTIALLY_REFUNDED]:
            raise forms.ValidationError(
                _('Setting charge status to {} directly '
                  'is not supported. Please use the dashboard to '
                  'refund partially.'.format(charge_status)),
                code='invalid_charge_status')

        return cleaned_data

    def get_payment_token(self):
        """Return selected charge status instead of token for testing only.
        Gateways used for production should return an actual token instead."""
        charge_status = self.cleaned_data['charge_status']
        return charge_status

        customer = _create_customer(request.user, customer_name, customer_phone)

        card = _create_card(customer, request.data)

        # Charge fee
        charge = customer.charges.create(
            method="card",
            device_session_id=request.data['session_id'],
            source_id=card.id,
            amount=amount,
            description="Fee Charge",
            order_id=get_random_string(length=12)
        )


def _create_customer(user, customer_name, customer_phone):
    if customer_name == '':
        customer_name = 'Undefined'
        customer = openpay.Customer.create(
<<<<<<< HEAD
        name=customer_name,
        email=getattr(user, 'email', "somebody@example.com"),
        last_name=getattr(user, 'last_name', "Unknown"),
        requires_account=False,
        phone_number=customer_phone
    )
    return customer
=======
            name=customer_name,
            email=getattr(user, 'email', "somebody@example.com"),
            last_name=getattr(user, 'last_name', "Unknown"),
            requires_account=False,
            phone_number=customer_phone
        )

        return customer
>>>>>>> 10a599bd180121a97c79de030f04398fb6a02334


def _create_card(customer, data):
    # create card
    card = customer.cards.create(
        card_number=data['number'],
        holder_name=data['name'],
        expiration_year=data['exp_year'],
        expiration_month=data['exp_month'],
        cvv2=data['cvv2'],
    )
    return card
