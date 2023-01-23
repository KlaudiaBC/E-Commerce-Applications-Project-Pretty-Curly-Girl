from django.db import models
from django.contrib.auth.models import User
from products.models import Product
from django.db.models.signals import post_save
from django.dispatch import receiver
from allauth.account.signals import user_signed_up
from birthday import BirthdayField

from django_countries.fields import CountryField


class UserProfile(models.Model):
    """
    A user profile model for maintaining default
    delivery information and order history
    """
    active_user.setdefault('is_active', True)

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=100, null=False, blank=False)
    default_phone = models.CharField(max_length=20, null=True, blank=True)
    birth_date = BirthdayField()
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)

    def __str__(self):
        return self.user.username


class Address(models.Model):
    """Delivery address"""
    user_profile = models.ForeignKey(UserProfile, verbose_name=(
        "User Profile"), on_delete=models.CASCADE)
    default_address_line_1 = models.CharField(
        max_length=80, null=True, blank=True)
    default_address_line_2 = models.CharField(
        max_length=80, null=True, blank=True)
    default_city = models.CharField(max_length=40, null=True, blank=True)
    default_postcode = models.CharField(max_length=20, null=True, blank=True)
    default_country = CountryField(
        blank_label='Country', null=True, blank=True)

    def __str__(self):
        return "Address"


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """
    if created:
        UserProfile.objects.create(user=instance)
    # Existing users: just save the profile
    instance.userprofile.save()
