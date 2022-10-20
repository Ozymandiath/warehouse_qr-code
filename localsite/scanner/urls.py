from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeProduct.as_view(), name="home"),
    path('login/', UserLogin.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('add/', AddProduct.as_view(), name="add"),
    path('register/', AddUser.as_view(), name="register"),
    path('profile/', OrderListParts.as_view(), name="profile"),
    path('parts/<int:pk>', DescriptionPart.as_view(), name="descripyion"),
    path('orderadd/<int:product_pk>/<int:user_pk>', SetOrderParts.as_view(), name="orderadd"),
    path('delete/<int:order_pk>', OrderDelete.as_view(), name="delete"),
]
