from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from rest_framework.decorators import api_view , permission_classes , authentication_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


from .models import *
from .serializer import *

@api_view(["GET"])
def All_Product_Detail(request):
    all_product = Product_detail.objects.all()
    serialize_product_deatil = Product_All_Detail_serializer_For_All(all_product , many=True)
    return Response(serialize_product_deatil.data)

@api_view(["GET"])
def All_Product_All_Detail(request):
    all_product = Product_detail.objects.all()
    serialize_product_deatil = Product_All_Detail_serializer(all_product , many=True)
    return Response(serialize_product_deatil.data)

@api_view(["GET"])
def product_info(request , pk):
    product_all_detail = Product_detail.objects.get(id = pk)
    serialized_product_detail = Product_All_Detail_serializer(product_all_detail , many=False)
    return Response(serialized_product_detail.data)

@api_view(["GET"])
def product_amount_detail(request , pk):
    product_all_detail = Product_detail.objects.get(id = pk)
    serialize_product_amount_data = product_Amount_Detail_serializer(product_all_detail , many=False)
    return Response(serialize_product_amount_data.data)


@api_view(["POST"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def update_product_info(request , pk):
    product_info = Product_detail.objects.get(id = pk)
    serialize_data = Product_deatil_serializer(instance = product_info ,data=request.data)
    if serialize_data.is_valid():
        try:
            serialize_data.save()
        except Exception as e:
            print(e)
        return Response([True , "Product Updated Successfully!!!" , "success"])

    return Response([False , "Product Update Unsuccessful!!!" , "error"])





# Product Why section

@api_view(["POST"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def create_product_why(request):
    #product_why = Product_Why.objects.get(od = pk)
    serialize_data = Product_why_serializer(data = request.data)
    if serialize_data.is_valid():
        serialize_data.save()
        return Response([True , dict(serialize_data.data)["id"] , "Product Why Created!!!" , "success"])
    return Response([False , "Product Why Created!!!" , "error"])

@api_view(["POST"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def update_product_why(request , pk):
    
    product_why_info = Product_Why.objects.get(id = pk)
    serialize_data = Product_why_serializer(instance=product_why_info ,data=request.data)

    if serialize_data.is_valid():
        serialize_data.save()
        return Response([True , dict(serialize_data.data)["id"] ,"Product Why Updated!!!" , "success"])
    return Response([False , "Product Why update Failed!!!" , "error"])

@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def delete_product_why(request , pk):
    try:
        product_why_info = Product_Why.objects.get(id = pk)
        product_why_info.delete()
        return Response([True , "Deleted Successfully!!!" , "success"])
    except Exception :
        return Response([False , "Delete Unsuccessful!!!" , "error"])

# Product Benefit's section

@api_view(["POST"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def create_product_benefit(request):
    #product_why = Product_benefit.objects.get(id = pk)
    serialize_data = Product_benefit_serializer(data = request.data)
    
    if serialize_data.is_valid():
        serialize_data.save()	 
        
        return Response([True , dict(serialize_data.data)["id"] , "Product Benefit Created!!!" , "success"])

    return Response([False , "Product Benefit Create Failed!!!" , "error"])


@api_view(["POST"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def update_product_benefit(request , pk):
    
    product_why_info = Product_benefit.objects.get(id = pk)
    serialize_data = Product_benefit_serializer(instance=product_why_info ,data=request.data)

    if serialize_data.is_valid():
        serialize_data.save()
        return Response([True , "Product Benefit Updated!!!" , "success"])
    return Response([False , "Product Benefit Update Failed!!!" , "error"])


@csrf_exempt
@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def delete_product_benefit(request , pk):
    try:
        product_why_info = Product_benefit.objects.get(id = pk)
        product_why_info.delete()
        return Response([True , "Product Benefit Delete Successful!!!" , "success"])
    except Exception :
        return Response([False , "Product Benefit Delete Failed!!!" , "error"])

# How to use

@api_view(["GET"])
def product_How_to_use_model(request , pk):
    product_how_to_use_detail = Product_how_to_use.objects.filter(product_id = pk)
    serialize_data = Product_How_to_use_serializer(product_how_to_use_detail , many=True)
    return Response(serialize_data.data)    


@api_view(["POST"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def product_How_to_use_model_create(request):
    serialize_data = Product_How_to_use_serializer(data = request.data)
    if serialize_data.is_valid():
        serialize_data.save()
        return Response([True , dict(serialize_data.data)["id"] , "Product How To Use Added!!!" , "success"])
    return Response([False , "Product How To Use Added Failed!!!" , "error"])    


@api_view(["POST"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def product_How_to_use_model_update(request , pk):
    all_product_how_to_use = Product_how_to_use.objects.get(id = pk)
    serialize_data = Product_How_to_use_serializer(instance = all_product_how_to_use ,data = request.data)
    if serialize_data.is_valid():
        serialize_data.save()
        return Response([True , "Product How To Use Updated!!!" , "success"])
    return Response([False , "Product How To Use Update Failed!!!" , "error"])


@api_view(["DELETE"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def product_How_to_use_model_delete(request , pk):
    try:
        all_product_how_to_use = Product_how_to_use.objects.get(id = pk)
        all_product_how_to_use.delete()
        return Response([True , "Product How To Use Deleted!!!" , "success"])
    except Exception :
        return Response([False , "Product How To Use Delete Failed!!!" , "error"])
# image Views

@api_view(["GET"])
def Product_image_info(request , pk):
    product_images_detail = Product_Image.objects.filter(prdouct_id = pk)
    serialize_product_image = Product_image_serializer(product_images_detail , many=True)
    return Response(serialize_product_image.data)


# Brand Logo Image

@api_view(["GET"])
def Brand_image_info(request):
    product_images_detail = BrandLogo.objects.all()
    serialize_product_image = Brand_Logo_serializer(product_images_detail , many=True)
    return Response(serialize_product_image.data)


