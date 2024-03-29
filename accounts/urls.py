"""crm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('home/',home,name='home'),
    path('customer_page/',home_customer,name='home_customer'),
    path('home_admin/',home_admin,name='home_admin'),
    path('products/',products,name='products'),
    path('customer/<str:customer_id>',customer,name='customer'),
    path('create_order/<str:customer_id>',createOrder,name='create_order'),
    path('update_order/<str:order_id>',updateOrder,name='update_order'),
    path('delete_order/<str:order_id>',deleteOrder,name='delete_order'),
    path('profile/',customerProfile,name='customer_profile'),
]
