from django.urls import path
from . import views
from django.views.generic import TemplateView


urlpatterns = [
    # User dashboard
    path("dashboard", views.dashboard, name="dashboard"),
    # Wishlist
    path('add_wishlist', views.add_wishlist, name='add_wishlist'),
    path('wishlist-my', views.wishlist, name='wishlist'),
]
