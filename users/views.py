from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.generic import CreateView

from .models import UserProfile, Wishlist, RefundView
from .forms import UserProfileForm, RefundForm
from products.models import Product


def dashboard(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            messages.success(request, 'Profile updated successfully')

    form = UserProfileForm(instance=profile)

    template = 'users/dashboard.html'
    context = {
        'form': form,
        'on_profile_page': True
    }

    return render(request, template, context)


@login_required
def wishlist(request):
    wlist = Wishlist.objects.filter(user=request.user).order_by('-id')
    return render(request, 'users/my_wishlist.html', {'wlist': wlist})


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


def refund_view(request):

    if request.method == 'POST':
        form = RefundForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Your request has been sent!\
                We will contact you shortly.')

    form = RefundForm()

    template = 'users/refund.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
