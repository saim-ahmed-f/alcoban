from django.db import models

# Create your models here.

from django.contrib.auth.models import User

from product_api.models import Product_detail

class Product_Review(models.Model):
    user_info = models.ForeignKey(User, related_name="user_info" , on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product_detail , related_name="product_info" , on_delete=models.CASCADE)
    main_title = models.CharField(max_length=50)
    star_value = models.FloatField()
    review_body = models.TextField(blank=True , null = True)

    def __str__(self):
        return self.main_title


