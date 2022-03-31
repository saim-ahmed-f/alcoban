
from django.urls import path

from .views import *

urlpatterns = [
    path('product_detail/AllProductDetail/' , All_Product_Detail , name="All Product Detail's"),
    path("product_detail/AllProductAllDetail/", All_Product_All_Detail, name="All Product All Detail's"),
    
    path('product_detail/<int:pk>/' , product_info , name="Product Info"),
    path("product_amount_deatil/<int:pk>/" , product_amount_detail , name="Product Amount Details"),
    path("product_update/per_Product/<int:pk>/" , update_product_info , name="Product detail update"),

    # why section
    
    path('product_why_create/' , create_product_why , name="Product create Why" ),
    path("product_why_update/<int:pk>/" , update_product_why , name="Product update Why"),
    path("product_why_delete/<int:pk>/" , delete_product_why , name="Product delete Why"),

    # benefit section

    path("product_benefit_create/" , create_product_benefit , name="product benefit create"),
    path("product_benefit_update/<int:pk>/" , update_product_benefit , name="Product benefit update"),
    path("product_benefit_delete/<int:pk>/", delete_product_benefit , name="Product benefit delete"),

    # How To Use

    path("product_How_to_Use_create/" , product_How_to_use_model_create , name="product How To Use create"),
    path("product_How_to_Use_update/<int:pk>/" , product_How_to_use_model_update , name="Product How To Use update"),
    path("product_How_to_Use_delete/<int:pk>/", product_How_to_use_model_delete , name="Product How To Use delete"),

    # Image Url

    path('product_detail/images/<int:pk>/' , Product_image_info , name="Product Images"),

    # Brand Logo Image 
    path("brand_logo/" , Brand_image_info , name="Brand Logo"),

]