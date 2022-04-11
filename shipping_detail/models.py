from django.db import models

# Create your models here.



class shipping_detail(models.Model):
    
    name = models.CharField(max_length=50)
    email = models.EmailField()
    #phone = models.CharField(max_length=12 , null=True)
    address = models.TextField()
    city = models.CharField(max_length=50)
    pincode = models.PositiveIntegerField()
    state = models.CharField(max_length=50)  
    

    def __str__(self):
        return self.name
