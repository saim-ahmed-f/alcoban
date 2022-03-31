from rest_framework import serializers

from .models import *


class Product_why_serializer(serializers.ModelSerializer):
    class Meta : 
        model = Product_Why
        fields = "__all__"


class Product_benefit_serializer(serializers.ModelSerializer):
    class Meta : 
        model = Product_benefit
        fields = "__all__"

class Product_deatil_serializer(serializers.ModelSerializer):
    class Meta:
        model = Product_detail
        fields = "__all__"       

class Product_image_serializer(serializers.ModelSerializer):
        class Meta:
            model = Product_Image
            fields = ["id" , "get_image" , "alt"]

class Product_How_to_use_serializer(serializers.ModelSerializer):
    class Meta:
        model = Product_how_to_use
        fields = ["id" , "how_to_use" , "product_id"]

class Product_All_Detail_serializer(serializers.ModelSerializer):
    product_why = Product_why_serializer(many = True , read_only = True)
    product_benefit = Product_benefit_serializer(many = True , read_only = True)
    prdouct_image = Product_image_serializer(many=True , read_only=True)
    product_how_to_use = Product_How_to_use_serializer(many=True , read_only=True)
    class Meta:
        model = Product_detail
        fields = [ "id" , "web_heading" , "product_name" , "product_price" , "product_online_price" , "delivery_charge" , "discount_value" , "product_about" , "product_why" , "product_benefit" , "prdouct_image" , "product_how_to_use"]


class product_Amount_Detail_serializer(serializers.ModelSerializer):
    class Meta :
        model = Product_detail
        fields = ["id" , "web_heading" , "product_name" , "product_price" , "product_online_price" , "delivery_charge" , "discount_value"]


class Product_All_Detail_serializer_For_All(serializers.ModelSerializer):
    prdouct_image = Product_image_serializer(many=True , read_only=True)
    class Meta:
        model = Product_detail
        fields = [ "id" , "product_name" , "product_price" , "product_online_price" , "delivery_charge" , "discount_value" , "product_about" , "prdouct_image"]



class Brand_Logo_serializer(serializers.ModelSerializer):
    class Meta:
        model = BrandLogo
        fields = ["id" , "get_Logo"]
