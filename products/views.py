from django.shortcuts import render
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