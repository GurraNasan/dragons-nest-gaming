import stripe

from django.shortcuts import render, reverse, redirect, get_object_or_404, HttpResponse
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm


def checkout(request):

    stripe_public_key = 'pk_test_51MTRe6FxabX2icHzmuEvA3nLRoxn5W79wupZuQeRu8Dh4l5skv4bKlohiHUsQ6aEPXvARQPfQygVUEPUDilNuvDy00Z7Jc1OEQ'
    # stripe_secret_key = settings.STRIPE_SECRET_KEY

    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, 'The cart is empty')
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': 'test client secret',
    }

    return render(request, template, context)