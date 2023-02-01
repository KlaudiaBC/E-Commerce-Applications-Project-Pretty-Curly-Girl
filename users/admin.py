from django.contrib import admin
from .models import UserProfile, Wishlist, RefundView


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = (
                    'user',
                    'default_phone',
                    'default_address_line_1',
                    'default_address_line_2',
                    'default_postcode',
                    'default_city',
                    'default_country')


@admin.register(Wishlist)
class UserWishlist(admin.ModelAdmin):
    list_display = ('user', 'product')


@admin.register(RefundView)
class AcceptRefund(admin.ModelAdmin):
    list_display = ('reference', 'message', 'email', 'accepted')
    list_filter = ('accepted', 'email')
