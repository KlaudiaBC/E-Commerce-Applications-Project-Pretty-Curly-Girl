from django.urls import path
from . import views

urlpatterns = [
    path('', views.users, name='profile'),
    # Wishlist
    path('wishlist-my', views.wishlist, name='wishlist'),
    path('add_wishlist', views.add_wishlist, name='add_wishlist'),
]
