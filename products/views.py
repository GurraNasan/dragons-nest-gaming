from django.shortcuts import render, get_object_or_404
from .models import Product


def products_list(request):
    """ 
        A view for all products and functionality for search and filtering by categories.
        insperied by Boutique Ado project in Code institute course
    """
    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)


def product_info(request, product_id):
    """ 
        A view for a singel product info
    """
    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_info.html', context)