from django.shortcuts import render,Http404,get_object_or_404
from django.views.generic import ListView,DetailView
from products.models import Product,Category

# Create your views here.
def home(request):
    return render(request, 'products/home.html', {'username':'Justin'})

def product_list(request):
    categories = Category.objects.all()
    products=Product.objects.all()
    context={'categories':categories,'products':products}
    return render(request,'products/product_list.html',context)

def product_list_by_category(request,slug=None):
    categories = Category.objects.all()
    products = Product.objects.all()
    if slug != None:
        category = Category.objects.get(slug=slug)
        products = Product.objects.filter(category=category)

    context = {
        'category': category,
        'categories': categories,
        'products': products
    }
    return render(request, 'products/product_list.html', context)

def ProductDetail(request,pk):
    try:
        product=Product.objects.get(pk=pk)
        return render(request,'products/product_detail.html',{'product':product})

    except:
        raise Http404

def Search(request):
    try:
        search=request.GET.get('search')
    except:
        search=None
    if search:
        products=Product.objects.filter(title__contains=search)
        context={'query':search,'products':products}
        template='products/results.html'
    else:
        template='products/product_list.html'
        context={}
    return render(request,template,context)
