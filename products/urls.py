from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<product_id>', views.product_detail, name='product_detail'),
    path('<product_pk>/review',
         views.AddReview.as_view(), name="add_review"),
    path('update/<slug:pk>', views.UpdateReview.as_view(),
         name="update_review"),
    path('delete/<slug:pk>', views.DeleteReview.as_view(),
         name="delete_review"),
]
