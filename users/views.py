from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from django.views.generic import CreateView

from .models import UserProfile, Wishlist, RefundView, ReviewProduct
from .forms import UserProfileForm, RefundForm, ReviewForm
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
            form.save()
            return render(request, 'users/refund_success.html')
    form = RefundForm()
    context = {'form': form}
    return render(request, 'users/refund.html', context)


class AddReview(CreateView):
    """
    Define attributes for the add review form,
    which will render in specified html file.
    """
    model = ReviewProduct
    form_class = ReviewForm
    template_name = 'users/add_review.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.product_id = self.kwargs['product_pk']
        messages.info(self.request, 'Thank You! Your review has been added.')

        return super().form_valid(form)


class UpdateReview(UpdateView):
    """
    Define attributes for the edit review,
    which will render in specyfied html file.
    """
    model = ReviewProduct
    form_class = ReviewForm
    template_name = "users/update_review.html"
    success_url = reverse_lazy('products')

    def form_valid(self, form):
        form.instance.review_id = self.kwargs['pk']
        messages.success(self.request, 'All changes have been saved!')

        return super().form_valid(form)


class DeleteReview(DeleteView):
    """
    Define attributes for the delete review,
    which will render in specyfied html file.
    """
    model = ReviewProduct
    template_name = "users/delete_review.html"
    success_url = reverse_lazy('products')
