from django.db import models

# Create your models here.



class Product_detail(models.Model):
    web_heading = models.CharField(max_length=100 , blank=True , null=True)
    product_name = models.CharField(max_length=50)
    product_price = models.IntegerField()
    product_about = models.TextField(blank=True , null=True)
    product_online_price = models.PositiveIntegerField(blank=True , null=True)
    delivery_charge = models.PositiveIntegerField(blank=True , null=True)
    discount_value = models.PositiveIntegerField(blank=True , null=True)

    def __str__(self):
        return self.product_name


class Product_Why(models.Model):
    product_id = models.ForeignKey(Product_detail , related_name="product_why" , on_delete=models.CASCADE)
    why_to_choose = models.CharField(max_length=50)

    def __str__(self):
        return self.why_to_choose



class Product_benefit(models.Model):
    product_id = models.ForeignKey( Product_detail , related_name="product_benefit", on_delete=models.CASCADE)
    product_benefit =  models.CharField(max_length=50)

    def __str__(self):
        return self.product_benefit




class Product_Image(models.Model):
    prdouct_id = models.ForeignKey(Product_detail , related_name="prdouct_image" , on_delete=models.CASCADE)
    product_images = models.ImageField(upload_to = "uploads/" , blank=True , null=True)
    alt = models.CharField(max_length=20 , blank=True , null=True)

    

    def get_image(self):
        if self.product_images:
            return "https://alcoban-vbk7q.ondigitalocean.app" + self.product_images.url


class Product_how_to_use(models.Model):
    product_id = models.ForeignKey(Product_detail  , related_name="product_how_to_use", on_delete=models.CASCADE)
    how_to_use = models.CharField(max_length=200, blank=True , null=True )
    def __str__(self):
        return self.how_to_use



class BrandLogo(models.Model):
    Brand_logo = models.ImageField(upload_to = "logo/" , blank=True , null=True)
    def get_Logo(self):
        if self.Brand_logo:
            return "http://127.0.0.1:8000" + self.Brand_logo.url