from django.urls import path

from .views import *

urlpatterns = [
    path("All_order_details/" , All_order_detail , name="All Order Detail"),
    path("create_shipping_detail/" , create_shipping_detail , name="create Shipping detail's"),
    path("update_shipping_detail/<int:pk>/" , update_shipping_detail , name="Update Shipping Detail's"),
    path("delete_shipping_detail/<int:pk>/" , delete_shipping_detail , name="Delete Shipping Detail's"),

    # Shipping Analysis
    path("Shipping_anaylsis/" , shippingAnaylsis , name="Pincode Anaylsis")
]