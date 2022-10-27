from django.shortcuts import render, get_object_or_404
from .models import Product


def all_products(request):
    """ A view to show the list view of the products """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show the detail view of the product """

    products = get_object_or_404(Product, pk=product_id)

    context = {
        'products': products,
    }

    return render(request, 'products/product-detail.html', context)
