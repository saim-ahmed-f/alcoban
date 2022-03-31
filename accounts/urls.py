from django.urls import path

from .views import *

urlpatterns = [
    path('login-user/<str:user_name>/<str:pass_word>/' , login_function , name="user login"),
    path('login-user/<str:user_name>/' , login_username , name="Token by username"),
    path('Logout-user/' , logout_view , name="Logout"),
]