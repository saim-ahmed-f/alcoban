from django.contrib import admin

# Register your models here.

from .models import *


admin.site.register(Product_detail)
admin.site.register(Product_Why)
admin.site.register(Product_benefit)
admin.site.register(Product_Image)
admin.site.register(Product_how_to_use)
admin.site.register(BrandLogo)