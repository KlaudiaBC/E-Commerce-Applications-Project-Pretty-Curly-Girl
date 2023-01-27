from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import UserProfile, Wishlist
from .forms import UserProfileForm
from products.models import Product
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
    if request.user.is_authenticated:
        data = Wishlist.objects.filter(
            user_id=request.user.pk, product_id=int(
                request.POST['attr_id']))
        if data.exists():
            Wishlist.objects.remove(
                user_id=request.user.pk),
            messages.info(
                request, 'This item has been removed from your wishlist.')
        else:
            Wishlist.objects.create(
                user_id=request.user.pk, product_id=int(
                    request.POST['attr_id'])),
            messages.info(
                request, 'Added item to your wishlist.'),

        return HttpResponse(status=200)
