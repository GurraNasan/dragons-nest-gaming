from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Product, Category


def products_list(request):
    """
        A view for all products and functionality for search and filtering by categories.
        insperied by Boutique Ado project in Code institute course
    """
    products = Product.objects.all()
    query = None
    sort = None
    direction = None

    if request.GET:
        """ Code for sorting """
        if 'sort' in request.GET:
            key = request.GET['sort']
            sort = key

            if key == 'name':
                key == 'lower_name'
                products = products.annotate(lower_name=Lower('name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    key = f'-{key}'
            products = products.order_by(key)

        """Code for filter out diffrent categories """
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        """Code for searchbar function """
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "I think you forgot to write anything, TRY AGAIN!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_sorting': current_sorting,
        'current_categories': categories,
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