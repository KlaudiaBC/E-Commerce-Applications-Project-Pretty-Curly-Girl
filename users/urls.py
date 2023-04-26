from django.urls import path
from . import views


urlpatterns = [
    # User dashboard
    path("dashboard", views.dashboard, name="dashboard"),
    # Wishlist
    path('add_wishlist', views.add_wishlist, name='add_wishlist'),
    path('wishlist-my', views.wishlist, name='wishlist'),
    path('refund', views.refund_view, name='refund'),
    # User Reviews
    path('<product_pk>/review',
         views.AddReview.as_view(), name="add_review"),
    path('update/<slug:pk>', views.UpdateReview.as_view(),
         name="update_review"),
    path('delete/<slug:pk>', views.DeleteReview.as_view(),
         name="delete_review"),
]
