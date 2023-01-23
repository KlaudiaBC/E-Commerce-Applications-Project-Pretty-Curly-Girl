from django.urls import path
from . import views
from django.views.generic import TemplateView


urlpatterns = [
    # User dashboard
    path("dashboard", views.dashboard, name="dashboard"),
    path('order_history/<order_number>', views.order_history,
         name='order_history'),
    path(
        "delete_user",
        TemplateView.as_view(
            template_name="delete_user.html"
            ), name="delete_confirmation",),
    # Wish List
    path("my_wishlist", views.wishlist, name="wishlist"),
    path("my_wishlist/<int:id>",
         views.add_to_wishlist, name="edit_wishlist"),
]
