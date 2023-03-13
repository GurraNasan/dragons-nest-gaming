from django.shortcuts import (
    render,
    redirect,
    reverse,
    get_object_or_404,
    HttpResponse,
)
from django.contrib import messages
from products.models import Product


def view_cart(request):
    """ A view for the cartpage"""
    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add a product to the cart """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
        messages.success(
            request, f'Updated {product.name} quantity to {cart[item_id]}'
        )
    else:
        cart[item_id] = quantity
        messages.success(request, f'Added {product.name} to your cart')

    request.session['cart'] = cart
    return redirect(redirect_url)


def adjust_cart(request, item_id):
    """ update quantity of a product in the cart """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[item_id] = quantity
        messages.success(
            request, f'Updated {product.name} quantity to {cart[item_id]}'
        )

    else:
        cart.pop(item_id)
        messages.success(
            request, f'Removed {product.name} from your cart'
        )

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def remove_from_cart(request, item_id):
    """ Remove product from cart """
    product = get_object_or_404(Product, pk=item_id)
    cart = request.session.get('cart', {})
    try: 
        cart.pop(item_id)
        messages.success(
            request, f'Removed {product.name} from your cart'
        )

        request.session['cart'] = cart
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, f'error removing item: {e}')
        return HttpResponse(status=500)
