from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django_countries.fields import CountryField


class UserProfile(models.Model):
    """
    A user profile model for maintaining default
    delivery information and order history
    """
    GENDER_CHOICES = [
        ('GENDER_MALE', 'Male'),
        ('GENDER_FEMALE', 'Female'),
        ('GENDER_OTHER', 'Other'),       
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birthdate = models.DateField(auto_now=False, null=True, blank=True)
    gender = models.PositiveSmallIntegerField(choices=GENDER_CHOICES,
                                              null=True, blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """
    if created:
        UserProfile.objects.create(user=instance)
    # Existing users: just save the profile
    instance.userprofile.save()
