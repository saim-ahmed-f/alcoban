from django.shortcuts import render

# Create your views here.

import datetime

import razorpay

from product_api.models import Product_detail


from .models import *
from .serializer import *

from rest_framework.decorators import api_view , permission_classes , authentication_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from django.views.decorators.csrf import csrf_exempt



@api_view(["GET"])
def show_order_deatil(request):
    all_order = order_detail.objects.all().order_by('-id')
    serialize_order_detail = basic_order_serializer(all_order , many=True)
    return Response(serialize_order_detail.data)


@api_view(["GET"])
def show_order_detail_limit(request , count):
    all_order = order_detail.objects.all().order_by('-id')[:count]
    serialize_order_detail = basic_order_serializer(all_order , many=True)
    return Response(serialize_order_detail.data)


@api_view(["GET"])
def show_order_by_type_detail(request , product_type):
    all_order = order_detail.objects.filter(order_states=product_type).order_by('-id')
    serialize_order = basic_order_serializer(all_order , many=True)
    return Response(serialize_order.data)


@api_view(["GET"])
def show_single_order_detail(request , pk):
    order = order_detail.objects.get(id = pk)
    serialize_order = basic_order_serializer(order , many=False)
    return Response(serialize_order.data)




@csrf_exempt
@api_view(["POST"])
def create_order_detail(request):
    serialize_order_data = create_order_serializer(data=request.data)
    if serialize_order_data.is_valid():
        serialize_order_data.save()
        return Response([True , "Order Have been Placed Successfully!!!" , "success"])
    
    return Response([False , "Placing Order Failed!!!" , "error"])




@api_view(["POST"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def update_order_detail(request , order_id):
    getting_order_details = order_detail.objects.get(id =  order_id)
    serialize_order_data = basic_order_update_serializer(instance=getting_order_details , data=request.data) 

    if serialize_order_data.is_valid():
        serialize_order_data.save()
        return Response([True , "Update Order Successfully!!!" , "success"])
    return Response([False , "Update Order Failed !!!" , "error"])




@api_view(["DELETE"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def delete_order_details(request , order_id):
    getting_order_to_delete = order_detail.objects.get(id = order_id)
    getting_order_to_delete.delete()
    return Response([True , "Deleted Successfully!!!" , "success"])





@api_view(["GET"])
def all_anaylsis_data(request):
    current_year = datetime.datetime.today().year
    data_fetch = []
    df = []
    count = 13

    for i in range(count):
        if i <10:
            df.append(order_detail.objects.filter(order_date__month = f"0{i}" , order_date__year = current_year).count())
        else:
            df.append(order_detail.objects.filter(order_date__month = f"{i}" , order_date__year = current_year).count())
    
    total_shipping_order = order_detail.objects.filter(order_states = "Shipped").count()
    total_pending_order = order_detail.objects.filter(order_states = "Pending").count()

    data_fetch.append(df)
    data_fetch.append(total_pending_order)
    data_fetch.append(total_shipping_order)
    data_fetch.append(int(total_shipping_order) + int(total_pending_order))
    return Response(data_fetch)


@api_view(["GET"])
def all_anaylsis_data_per_product(request):
    current_year = datetime.datetime.today().year
    df = []
    count = 13

    counter = 0
    all_product = Product_detail.objects.all()
    for i in all_product:
        df.append({"product_id" : i.id , "product_name" : i.product_name , "product_data" : []})
        for j in range(count):
            if j < 10:
                df[counter]["product_data"].append(order_detail.objects.filter(order_date__month = f"0{j}" , order_date__year = current_year , product_id = i.id).count())
                #df[f"{i.product_name}"].append(order_detail.objects.filter(order_date__month = f"0{j}" , order_date__year = current_year , product_id = i.id).count())
            else:
                df[counter]["product_data"].append(order_detail.objects.filter(order_date__month = f"{j}" , order_date__year = current_year , product_id = i.id).count())
                #df[f"{i.product_name}"].append(order_detail.objects.filter(order_date__month = f"{j}" , order_date__year = current_year , product_id = i.id).count())
        counter += 1

    return Response(df)








# Razor pay View

@api_view(["GET"])
def Rezorpay_create_order_id(request , quantity , product_id):

    getting_product_detail = Product_detail.objects.get(id = product_id)

    generating_amount = ((int(getting_product_detail.product_online_price) * int(quantity)) + int(getting_product_detail.delivery_charge)) * 100

    client = razorpay.Client( auth = ( "rzp_test_OmeeTYyShQf7Lg", "8qNcUWIkFt8s7X1SYzefY12N" ) )

    payment = client.order.create({'amount': generating_amount , 'currency': 'INR' , 'payment_capture': '1'})
     
    return Response(dict(payment))






