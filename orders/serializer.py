from rest_framework import serializers

from .models import *

from product_api.serializer import product_Amount_Detail_serializer
from shipping_detail.serializer import Shipping_Detail_serializer

class order_serializer(serializers.ModelSerializer):
    order_product_info_for_user = product_Amount_Detail_serializer(many=True , read_only=True)
    order_shipping_info_of_user = Shipping_Detail_serializer(many=True , read_only=True)
    class Meta:
        model = order_detail
        fields = ["id" , "user_id" , "order_product_info_for_user" , "order_shipping_info_of_user" , "order_date" , "payment_method" , "quantity" , "total_value" , "product_awb_no" ]

class basic_order_serializer(serializers.ModelSerializer):
    class Meta:
        model = order_detail
        fields = "__all__"
        depth = 1

class basic_order_update_serializer(serializers.ModelSerializer):
    class Meta :
        model = order_detail
        fields = "__all__"

class create_order_serializer(serializers.ModelSerializer):
    class Meta:
        model = order_detail
        fields = "__all__"
        