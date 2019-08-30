from django.shortcuts import render,HttpResponseRedirect,Http404
from django.urls import reverse
from .models import Cart,CartItem
from products.models import Product,Variation
from django.contrib.auth.decorators import login_required

# Create your views here.

def ViewCart(request):
    try:
        cid=request.session['cart_id']
        cart=Cart.objects.get(id=cid)
    except:
        cid=None
    if cid:
        new_total=0.0
        for item in cart.cartitems.all():
            line_total=float(item.product.price) * (item.quantity)
            new_total+=line_total
        request.session['cart_items_total']=cart.cartitems.count()
        print(request.session['cart_items_total'])
        cart.total=new_total
        cart.save()
        context={'cart':cart}
    if cid==None or request.session['cart_items_total'] == 0:
        empty_message='Your cart is empty Please continue shopping'
        context={'empty':True,'empty_message':empty_message}
    template='carts/view.html'
    return render(request,template,context)


def remove_cart(request,id):
    try:
        cid=request.session['cart_id']
        cart=Cart.objects.get(id=cid)
    except:
        cid=None
    cartItem=CartItem.objects.get(id=id)
    cartItem.delete()
    return HttpResponseRedirect(reverse('carts:view_cart'))


@login_required
def update_cart(request,slug):

    try:
        cid=request.session['cart_id']
    except:
        new_cart=Cart()
        new_cart.save()
        request.session['cart_id']=new_cart.id
        cid=request.session['cart_id']
    cart=Cart.objects.get(id=cid)
    try:
        product=Product.objects.get(slug=slug)
    except:
        raise Http404

    prod_var=[]
    if request.method=='POST':
        qty=request.POST['qty']
        for item in request.POST:
            # print(request.POST[item])
            try:
                v=Variation.objects.get(product=product,category__iexact=item,title__iexact=request.POST[item])
                prod_var.append(v)
                print(v)
            except:
                pass
        cart_item=CartItem.objects.create(cart=cart,product=product)
        if len(prod_var)>0:
            cart_item.variations.clear()
            for item in prod_var:
                cart_item.variations.add(item)
        cart_item.quantity=qty
                # cart_item.notes=notes
        cart_item.save()
        return HttpResponseRedirect(reverse('carts:view_cart'))
    else:
        return HttpResponseRedirect(reverse('carts:view_cart'))
