from django.urls import path
from .views import checkout,orders

app_name='orders'

urlpatterns=[
    path('checkout/',checkout,name='cart_checkout'),
    path('orders/',orders,name='orderlist')
]
