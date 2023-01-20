from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category, Review
from .forms import ReviewForm


def all_products(request):
    """ A view to show the list of the products """

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None
    sale = None

    """Allows to sort the products by price"""
    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        """Allow to sort the products by category"""
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'sale' in request.GET:
            products = products.filter(sale=True)

        """Search engine - iterates through
        the name of the product and its description"""
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Please enter your search criteria.")
                return redirect(reverse('products'))

            queries = (
                Q(name__icontains=query) | Q(description__icontains=query)
            )
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
        'current_sale': sale,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show the detail view of the product """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product-detail.html', context)


class AddReview(CreateView):
    """
    Define attributes for the add review form,
    which will render in specified html file.
    """
    model = Review
    form_class = ReviewForm
    template_name = 'products/add_review.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.review_id = self.kwargs['review_id']
        messages.info(self.request, 'Thank You! Your review has been added.')

        return super().form_valid(form)


class UpdateReview(UpdateView):
    """
    Define attributes for the Edit Post form,
    which will render in specyfied html file.
    """
    model = Review
    form_class = ReviewForm
    template_name = "products/update_review.html"
    success_url = reverse_lazy('products')

    def form_valid(self, form):
        form.instance.review_id = self.kwargs['pk']
        messages.success(self.request, 'All changes have been saved!')

        return super().form_valid(form)


class DeleteReview(DeleteView):
    """
    Define attributes for the delete post page,
    which will render in specyfied html file.
    """
    model = Review
    template_name = "products/delete_review.html"
    success_url = reverse_lazy('home')
