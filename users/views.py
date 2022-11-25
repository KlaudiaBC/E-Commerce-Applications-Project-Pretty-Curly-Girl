from django.shortcuts import render, get_object_or_404
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter

from django.contrib import messages

from .models import UserProfile
from .forms import UserProfileForm


def profiles(request):
    """ Display the user's profile. """

    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')

    form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True
    }

    return render(request, template, context)


class SocialAccountAdapter(DefaultSocialAccountAdapter):
    def save_user(self, request, sociallogin, form=None):
        user = super(SocialAccountAdapter, self).save_user(
            request, sociallogin, form)

        context = {
            'user': profile,
        }

        return user
