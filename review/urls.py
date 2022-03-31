from django.urls import path
from .views import *


urlpatterns = [
    path("review_detail/<int:product_id>/" , review_detail , name="All Product Review"),
    path("review_create/" , review_create_for_product , name="Create Product Review"),
    path("review_update/<int:pk>/" , review_update_for_product , name="Update Product Review"),
    path("review_delete/<int:pk>/", review_delete_for_product , name="delete Product review")
]