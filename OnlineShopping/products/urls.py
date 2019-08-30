from django.urls import path
from products.views import product_list_by_category,ProductDetail,Search,product_list

app_name='products'

urlpatterns=[
    path('',product_list,name='productlist'),
    path('category/<slug>/',product_list_by_category,name='products'),
    path('search/',Search,name='search'),
    path('products/<pk>/',ProductDetail,name='single_product')
]
