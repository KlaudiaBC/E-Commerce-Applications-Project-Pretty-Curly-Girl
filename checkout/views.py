from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51M2NH3IIiKDh22zFIfUeJZF5or1iKTB7np1Qs07mDSUsK5kFh0uI6AXgivoZ5XU8mZe2S5PvNUBEzsGaTJda8tcJ00ZAqlGsBN',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
