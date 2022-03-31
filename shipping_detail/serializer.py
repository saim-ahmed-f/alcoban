from rest_framework import serializers

from .models import *

class Shipping_Detail_serializer(serializers.ModelSerializer):
    class Meta:
        model = shipping_detail
        fields = "__all__"







