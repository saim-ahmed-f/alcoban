from django.shortcuts import render




# Create your views here.

from rest_framework.authtoken.models import Token

from django.contrib.auth import authenticate , login , logout

from django.contrib.auth.models import User


from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializers import *


@api_view(["POST"])
def login_function(request , user_name , pass_word):
    #user_name = un#"sam"#request.POST.get('username' , None)
    #pass_word = pw#"1407"#request.POST.get('password' , None)
    data = {}

    
    if user_name == "" or pass_word == "":
        return Response({"error" : "Please enter the username or password"} , status=status.HTTP_400_BAD_REQUEST)
    #data = None
    #if str(request.user) == str(user_name):
    #        return Response({"error" : "User Already login" , "data" : data} , status=status.HTTP_400_BAD_REQUEST)
    
    #if not user_name or not pass_word:
    #    return Response({"error" : "error no value entered" , "data" : data} , status=status.HTTP_400_BAD_REQUEST)
    
    checkUser = User.objects.filter(username = user_name).exists()
    if checkUser == False:
        return Response({"error" : "Username / password is invalid " , "data" : data} , status = status.HTTP_404_NOT_FOUND)
    
    user = authenticate(username = user_name , password = pass_word)
    if user is not None:
        login(request , user)
        token , create_null = Token.objects.get_or_create(user=request.user)
        data = {
            "token" : token.key,
            "user_id" : request.user.pk,
            "username" : request.user.username
        }
    else:
        return Response({"error" : "Username / password is invalid " , "Response_status" : "error" , "data" : data} , status = status.HTTP_404_NOT_FOUND)        
    
    return Response({"login" : "you are login" , "Response_status" : "success" , "data" : data} , status=status.HTTP_200_OK)


@api_view(["POST"])
def login_username(request , user_name):
    #user_name = un#"sam"#request.POST.get('username' , None)
    #pass_word = pw#"1407"#request.POST.get('password' , None)
    data = {}

    
    if user_name == "":
        return Response({"error" : "Please enter the username or password"} , status=status.HTTP_400_BAD_REQUEST)
    #data = None
    #if str(request.user) == str(user_name):
    #        return Response({"error" : "User Already login" , "data" : data} , status=status.HTTP_400_BAD_REQUEST)
    
    #if not user_name or not pass_word:
    #    return Response({"error" : "error no value entered" , "data" : data} , status=status.HTTP_400_BAD_REQUEST)
    
    checkUser = User.objects.filter(username = user_name).exists()
    if checkUser == False:
        return Response({"error" : "Username / password is invalid ", "Response_status" : "error" , "data" : data} , status = status.HTTP_404_NOT_FOUND)
    
    
    token , create_null = Token.objects.get_or_create(user=request.user)
    data = {
        "token" : token.key,
    }
    return Response({"login" : "you are login", "Response_status" : "success" , "data" : data} , status=status.HTTP_200_OK)


def logout_view(request):
    try:
        logout(request)
        return Response([True , "Logout Successfully!!!" , "success"])
    except Exception :
        return Response([True , "Not Able To Logout!!!" , "error"])