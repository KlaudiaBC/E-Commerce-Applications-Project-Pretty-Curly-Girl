from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import UserProfile, Wishlist
from .forms import UserProfileForm
from products.models import Product
import requests


@login_required
def users(request):
    """Display the user's profile and him allow to update"""

    user = get_object_or_404(UserProfile, user=request.user)
    orders = user.orders.all()

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request,
                           'Update failed. Please ensure the form is valid.')
    else:
        form = UserProfileForm(instance=user)

    template = 'users/profile.html'
    context = {
        'form': form,
        'on_profile_page': True
    }

    form = UserProfileForm(instance=user)

    return render(request, template, context)


def add_wishlist(request):
    if request.POST:
        if request.user.is_authenticated:
            data = Wishlist.objects.filter(
                user_id=request.user.pk, product_id=int(
                    request.POST['attr_id']))
            if data.exists():
                messages.error(
                    request, 'This item can not be added to your wishlist.')
            else:
                Wishlist.objects.create(
                    user_id=request.user.pk, product_id=int(
                        request.POST['attr_id'])),
                messages.info(
                    request, 'Added item to your wishlist.')

    return HttpResponse(status=200)


# My Wishlist
def wishlist(request):
    wlist = Wishlist.objects.filter(user=request.user).order_by('-id')
    return render(request, 'users/wishlist-my.html', {'wlist': wlist})
