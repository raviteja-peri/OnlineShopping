from django.urls import path
from carts.views import ViewCart,update_cart,remove_cart

app_name='carts'

urlpatterns=[
    path('',ViewCart,name='view_cart'),
    path('cart/<slug>/',update_cart,name='update_cart'),
    path('remove/<id>/',remove_cart,name='remove_cart')
]
