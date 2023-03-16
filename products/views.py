from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Product, Category, SubCategory
from .forms import ProductForm


def products_list(request):
    """
        A view for all products and functionality for search and filtering by categories.
        insperied by Boutique Ado project in Code institute course
    """
    products = Product.objects.all()
    query = None
    categories = None
    subcategories = None
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

        """Code for filter out diffrent subcategories """
        if 'sub_category' in request.GET:
            subcategories = request.GET['sub_category'].split(',')
            products = products.filter(sub_category__name__in=subcategories)
            subcategories = SubCategory.objects.filter(name__in=subcategories)

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
        'current_subcategories': subcategories,
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


def add_product(request):
    """
        A view for adding products
    """

    if not request.user.is_superuser:
        messages.error(request, 'Can´t do that, need to be a Administrator \
            to do that')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Product added!')
            return redirect(reverse('product_info', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. \
                Please ensure the form is valid')
    else:
        form = ProductForm()

    template = 'products/add_products.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def edit_product(request, product_id):
    """
        view to edit a product
    """
    if not request.user.is_superuser:
        messages.error(request, 'Can´t do that, need to be a Administrator \
            to do that')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, f'Successfully updated product \
                {product.name}!')
            return redirect(reverse('product_info', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. \
                Please ensure the form is valid')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_products.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


def delete_product(request, product_id):
    """
        view to delete product
    """
    if not request.user.is_superuser:
        messages.error(request, 'Can´t do that, need to be a Administrator \
            to do that')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, f'Product {product.name} \
        has been deleted!')
    return redirect(reverse('product_info'))
