from django.shortcuts import render

# Create your views here.


from .models import *
from .serializer import *


from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET"])
def review_detail(request , product_id):
    all_review = Product_Review.objects.filter(product_id = product_id)
    
    serialize_data = review_serializer(all_review , many=True)
    return Response(serialize_data.data)


@api_view(["POST"])
def review_create_for_product(request):
    serialize_data = review_serializer(data=request.data)
    if serialize_data.is_valid():
        serialize_data.save()
    return Response(True)


@api_view(["POST"])
def review_update_for_product(request , pk):
    review_detail = Product_Review.objects.get(id = pk)
    serialize_data = review_serializer(instance=review_detail , data=request.data)
    if serialize_data.is_valid():
        serialize_data.save()
    return Response(True)


@api_view(["DELETE"])
def review_delete_for_product(request , pk):
    review_detail = Product_Review.objects.get(id = pk)
    review_detail.delete()
    return Response(True)

