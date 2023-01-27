from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import UserProfile, Wishlist
from .forms import UserProfileForm
from checkout.models import Order


def dashboard(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')

    form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'users/dashboard.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True
    }

    return render(request, template, context)


def order_history(request, order_number):
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
    products = Wishlist.objects.filter(user=request.user).order_by('-id')
    return render(request, "users/my_wishlist.html", {
        "wishlist": products})


@login_required
def add_to_wishlist(request, id):
    product = get_object_or_404(Product, id=id)
    if product.Wishlist.filter(id=request.user.id).exists():
        product.Wishlist.remove(request.user)
        messages.info(
            request, f'{product.title} has been removed from your WishList.')
    else:
        product.Wishlist.add(request.user)
        messages.success(
            request, f'Added {product.title} to your WishList.')
    return render(request, "users/my_wishlist/<int:id>.html")
