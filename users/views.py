from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages

from .models import UserProfile
from .forms import UserProfileForm
from products.models import Product
from .models import Wishlist
import requests

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5)\
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}


@login_required
def users(request):
    """ Display the user's profile and him allow to update"""

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


# # Add product to Wishlist
# def add_wishlist(request):

#     if request.is_ajax() and request.POST:
#         if request.user.is_authenticated:
#             data = Wishlist.objects.filter(
#                 user_id=request.user.pk, product_id=int(
#                     request.POST['attr_id']))
#             if data.exists():
#                 error: sayno()
#             else:
#                 success: sayyes()
#                 Wishlist.objects.create(
#                     user_id=request.user.pk, product_id=int(
#                         request.POST['attr_id']))

#     return HttpResponse(status=200)


# My Wishlist
def wishlist(request):
    wishlist = Wishlist.objects.filter(user=request.user).order_by('-id')
    return render(request, 'users/wishlist-my.html', {'wishlist': wishlist})


def add_wishlist(request, pk):
    """
    Define the function that toggle button
    'like' and 'unlike' for a specific product
    and accordingly add/remove this product from users wish list
    """
    wish_item = get_object_or_404(Product, id=request.POST.get('product_id'))
    wishlist = Wishlist.objects.filter(user=request.user)
    liked = False

    if user.is_authenticated:
        if wish_item in wishlist():
            wishlist.objects.remove(wish_item)
            liked = False
            messages.danger(request,
                            f"Removed {wish_item.name} from your wishlist!")
        else:
            wishlist.objects.add(wish_item)
            liked = True
            messages.success(request, f"Added {wish_item.name}\
                to your wishlist!")
            return HttpResponse(200)
    else:
        messages.info(request, "You must login to access wishlist!")
        return HttpResponse(200)
