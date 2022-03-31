from rest_framework import serializers

from .models import *


class review_serializer(serializers.ModelSerializer):
    class Meta:
        model = Product_Review
        fields = "__all__" 
        
