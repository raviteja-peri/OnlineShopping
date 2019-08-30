from django.db import models
from products.models import Product,Variation

# Create your models here.


class Cart(models.Model):
    # items=models.ManyToManyField(CartItem,null=True,blank=True)
    # products=models.ManyToManyField(Product,null=True,blank=True)
    total=models.DecimalField(max_digits=100,decimal_places=2,default=0.0)
    timestamp=models.DateTimeField(auto_now_add=True,auto_now=False)
    updated_date=models.DateTimeField(auto_now_add=False,auto_now=True,null=True,blank=True)
    active=models.BooleanField(default=True)

    def __str__(self):
        return "Cart Id:{}".format(self.id)

class CartItem(models.Model):
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE,related_name='cartitems',null=True,blank=True)
    product=models.ForeignKey(Product,on_delete=models.CASCADE,null=True,blank=True)
    quantity=models.IntegerField(default=1)
    variations=models.ManyToManyField(Variation,null=True,blank=True)
    line_total=models.DecimalField(max_digits=1000,decimal_places=2,default=0.00)
    notes=models.TextField(null=True,blank=True)
    timestamp=models.DateTimeField(auto_now_add=True,auto_now=False)
    updated_date=models.DateTimeField(auto_now_add=False,auto_now=True,null=True,blank=True)

    def __str__(self):
        return self.product.title
