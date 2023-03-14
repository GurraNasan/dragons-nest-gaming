from django.shortcuts import render, reverse, redirect, get_object_or_404, HttpResponse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, 'The cart is empty')
        return redirect(reverse('products'))

    order_form = Orderform()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
    }

    return render(request, template, context)