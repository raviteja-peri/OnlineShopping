from django.db import models
from carts.models import Cart
from django.contrib.auth import get_user_model

User=get_user_model()

# Create your models here.
status_choices=(
('Started','Started'),
('Shipped','Shipped'),
('Delivered','Delivered')
)

class Order(models.Model):
    user=models.ForeignKey(User,related_name='orders',on_delete=models.CASCADE,blank=True,null=True)
    order_id=models.CharField(max_length=120,default='ABC',unique=True)
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
    sub_total=models.DecimalField(max_digits=1000,decimal_places=2,default=0.00)
    tax_total=models.DecimalField(max_digits=1000,decimal_places=2,default=0.00)
    final_price=models.DecimalField(max_digits=1000,decimal_places=2,default=0.00)
    status=models.CharField(max_length=120,choices=status_choices,default='Started')
    timestamp=models.DateTimeField(auto_now_add=True,auto_now=False)
    updated_date=models.DateTimeField(auto_now_add=False,auto_now=True,null=True,blank=True)

    def __str__(self):
        return self.order_id
