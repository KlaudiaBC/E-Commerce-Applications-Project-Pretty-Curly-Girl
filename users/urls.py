from django.urls import path
from . import views


urlpatterns = [
    # User dashboard
    path("dashboard", views.dashboard, name="dashboard"),
    # Wishlist
    path('add_wishlist', views.add_wishlist, name='add_wishlist'),
    path('wishlist-my', views.wishlist, name='wishlist'),
    path('refund', views.refund_view, name='refund'),
]
