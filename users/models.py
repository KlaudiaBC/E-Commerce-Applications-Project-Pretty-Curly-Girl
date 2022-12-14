from django.db import models
from django.contrib.auth.models import User
from products.models import Product
from django.db.models.signals import post_save
from django.dispatch import receiver
from allauth.account.signals import user_signed_up


class UserProfile(models.Model):
    """
    A user profile model for maintaining default
    delivery information and order history
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=254, null=True, blank=True)
    birthdate = models.DateField(auto_now=False, null=True, blank=True)

    def __str__(self):
        return self.user.username

    @receiver(user_signed_up)
    # Populate a user who signed up via social account
    def populate_profile(sociallogin, user, **kwargs):

        user.profile = UserProfile()

        if sociallogin.account.provider == 'google':
            user_data = user.socialaccount_set.filter(
                provider='google')[0].extra_data
            email = user_data['email']
            user = user_data['name']

        user.userprofile.email = email
        user.userprofile.name = user
        user.profile.save()


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """
    if created:
        UserProfile.objects.create(user=instance)
    # Existing users: just save the profile
    instance.userprofile.save()


class Wishlist(models.Model):
    """
    Create a list of favourite products
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
