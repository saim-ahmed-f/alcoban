from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User

from .models import * 
from .serializer import *

from django.views.decorators.csrf import csrf_exempt

from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.db.models import Count



@api_view(["GET"])
def All_order_detail(request):
    order_detail = shipping_detail.objects.all()
    all_order_serializer = Shipping_Detail_serializer(order_detail , many=True)
    return Response(all_order_serializer.data)

@api_view(["GET"])
def Show_shipping_detail(request , pk):
    
    shipping_details = shipping_detail.objects.get(user_id=pk)
    serialize_data = Shipping_Detail_serializer(shipping_details , many=False)

    return Response(serialize_data.data)


@csrf_exempt
@api_view(['POST'])
def create_shipping_detail(request):
    serializer_shipping = Shipping_Detail_serializer(data=request.data)
    if serializer_shipping.is_valid():
        serializer_shipping.save()
        return Response([True , dict(serializer_shipping.data)["id"]])
    return Response(False)


@api_view(['POST'])
def update_shipping_detail(request , pk):
    shipping_detail = shipping_detail.objects.get(id = pk)
    serialize_shipping = Shipping_Detail_serializer(instance=shipping_detail , data = request.data)
    if serialize_shipping.is_valid():
        serialize_shipping.save()
        return Response(True)
    return Response(False)


@api_view(['DELETE'])
def delete_shipping_detail(request , pk):
    shipping_detail = shipping_detail.objects.get(id = pk)
    shipping_detail.delete()
    return Response(True)



@api_view(['GET'])
def shippingAnaylsis(request):

    queryset = shipping_detail.objects.values('pincode' , "city").annotate(count = Count('pincode'))


    return Response(queryset)
