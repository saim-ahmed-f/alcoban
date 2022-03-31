from django.db import models

# Create your models here.
from django.contrib.auth.models import User

from product_api.models import Product_detail
from shipping_detail.models import shipping_detail





class order_detail(models.Model):
    
    product_id = models.ForeignKey(Product_detail , related_name="order_product_info_for_user" , on_delete=models.CASCADE)
    shipping_id = models.ForeignKey(shipping_detail , related_name="order_shipping_info_of_user" , on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True , blank=True)
    payment_method = models.BooleanField()
    quantity = models.PositiveIntegerField()
    total_value = models.PositiveIntegerField()

    states_value = (("Pending" , "Pending") , ("Shipped" , "Shipped") , ("Delivered" , "Delivered") , ("Returned" , "Returned"))
    order_states = models.CharField(max_length=10 , choices=states_value , default="Pending" , blank=True , null = True)

    razorpay_order_id = models.CharField(max_length=500 , blank=True , null=True)
    razorpay_payment_id = models.CharField(max_length=500 , blank=True , null=True)
    razorpay_signature = models.CharField(max_length=500 , blank=True , null=True)
    product_awb_no = models.CharField(max_length=500 , blank=True , null=True)