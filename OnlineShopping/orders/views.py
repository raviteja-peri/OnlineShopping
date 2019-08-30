from django.shortcuts import render, HttpResponseRedirect
from carts.models import Cart
from .models import Order
from orders.utils import id_generator
from django.urls import reverse
from django.contrib.auth.decorators import login_required
import time
# Create your views here.

def orders(request):
    template='orders/orderlist.html'
    context={}
    return render(request,template,context)

@login_required
def checkout(request):
    try:
        cid=request.session['cart_id']
        cart=Cart.objects.get(id=cid)
    except:
        cid=None
        return HttpResponseRedirect(reverse('carts:view_cart'))
    try:
        new_order=Order.objects.get(cart=cart)
    except:
        new_order,created=Order.objects.get_or_create(cart=cart)
        if created:
            new_order.order_id=id_generator()
            new_order.user=request.user
            new_order.save()

    if new_order.status =='Delivered':
        cart.delete()
        del request.session['cart_id']
        del request.session['cart_items_total']

    template='orders/order_detail.html'
    context={'order':new_order}
    return render(request,template,context)
