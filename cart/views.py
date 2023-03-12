from django.shortcuts import render


def view_cart(request):
    """ A view for the cartpage"""
    return render(request, 'cart/cart.html')
