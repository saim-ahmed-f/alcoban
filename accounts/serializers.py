from rest_framework import serializers
from  django.contrib.auth.models import User

from rest_framework.authtoken.models import Token

from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model : User
        fields="__all__"


class TokenResponse(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields= "__all__"


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username' , 'password')