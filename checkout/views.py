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
        'stripe_public_key': 'pk_test_51MYAZSB7wxoQRYe9J5kXNaJRMocJwMqazCqiZRIDncw9NJiPeguTq9g2qxNdsy6CyakMK9bFLQd3qNIOXLk7rBXV00g4dxFK2q',
        'client_secret': 'sk_test_51MYAZSB7wxoQRYe9Xd8zjB8L4OD1qNOvYMl875bOTiLIH74RnVwfNeyPUls9vH5uxVWSX9TGJV5cr8oc7XlnS6TG004B0DbSeb',
    }

    return render(request, template, context)
