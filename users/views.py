from django.shortcuts import render, get_object_or_404

from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import UserProfile
from .forms import UserProfileForm
from checkout.models import Order

from products.models import Product


@login_required
def users(request):
    """ Display the user's profile. """

    user = get_object_or_404(UserProfile, user=request.user)

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
    orders = user.orders.all()

    template = 'users/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True
    }

    form = UserProfileForm(instance=user)

    return render(request, template, context)
