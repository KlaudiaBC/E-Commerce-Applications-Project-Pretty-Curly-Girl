from django.contrib import admin
from .models import UserProfile, Wishlist


@admin.register(Wishlist)
class UserWishlistAdmin(admin.ModelAdmin):
    list_display = ('user', 'wish_item')


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user',)
