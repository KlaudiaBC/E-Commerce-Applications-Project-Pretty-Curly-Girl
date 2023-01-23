from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import UserProfile, Wishlist
from .forms import UserProfileForm
from products.models import Product
from checkout.models import Order

import request


def dashboard(request):
    """Display the user's profile."""
    profile = get_object_or_404(UserProfile, user=request.user)
    address = get_object_or_404(Address, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
    form_user = UserProfileForm(instance=profile)

    if request.method == 'POST':
        form = AddressForm(request.POST, instance=address)
        if form.is_valid():
            form.save()
            messages.success(request, 'Address updated successfully')
    form_address = AddressForm(instance=address)

    orders = profile.orders.all()

    template = 'users/dashboard.html'
    context = {
        'form_user': form_user,
        'form_address': form_address,
        'orders': orders,
        'on_profile_page': True
    }

    return render(request, template, context)


def order_history(request, order_number):
    """Display the order history."""
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)


@login_required
def wishlist(request):
    """Display the user's wishlist."""
    products = Product.objects.filter(users_wishlist=request.user)
    return render(request, "users/my_wishlist.html", {"wishlist": products})


@login_required
def add_to_wishlist(request, id):
    """Add/Remove product to/from the wishlist"""
    product = get_object_or_404(Product, id=id)
    if product.users_wishlist.filter(id=request.user.id).exists():
        product.users_wishlist.remove(request.user)
        messages.info(
            request, f'{product.title} has been removed from your WishList.')
    else:
        product.users_wishlist.add(request.user)
        messages.success(
            request, f'Added {product.title} to your WishList.')
    return HttpResponseRedirect(request.META["HTTP_REFERER"])


@login_required
def delete_user(request):
    """Remove User Profile"""
    user = UserProfile.objects.get(user_name=request.user)
    user.is_active = False
    user.save()
    logout(request)
    return redirect("users:delete_confirmation")
