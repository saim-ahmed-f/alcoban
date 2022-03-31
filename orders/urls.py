from django.urls import path

from .views import *

urlpatterns = [
    path("All Order/" , show_order_deatil , name="Show All Order's"),
    path("orderType/<str:product_type>/" , show_order_by_type_detail , name="Order's By Type"),
    path("product_detail/single_order/<int:pk>/", show_single_order_detail, name="Single Order Detail's"),
    path("product_detail_by_limit/<int:count>/", show_order_detail_limit, name="Order Detail's By Limit"),
    


    path("Create_Basic_Order/" , create_order_detail , name="Create Order"),
    path("Update order/<int:order_id>/" , update_order_detail , name="Update Order Detail"),
    path("Delete Order/<int:order_id>/" , delete_order_details , name="Delete Order Detail"),

    path("OrderData/anaylsis/" , all_anaylsis_data , name="test"),
    path("OrderData/anaylsis/perPrdouct/" , all_anaylsis_data_per_product , name="test"),


    # Rezor Pay Url

    path("Razorpay_Order_creation/<int:quantity>/<int:product_id>/" , Rezorpay_create_order_id , name="Rezor Pay Order Id Creation")

]