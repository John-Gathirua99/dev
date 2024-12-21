from django.shortcuts import render

# Create your views here.

from .models import Product,Category,Customer,Orders
from django.contrib import messages

from django.views.generic import DetailView,DeleteView,CreateView,ListView

def home(request):

    products = Product.objects.all()

    context = {'products':products}

    return render(request,'store/home.html',context)

def about(request):
    return render(request,'store/about.html',{})

def product(request,pk):
    
    products = Product.objects.get(id=pk)

    context = {'products':products}

    return render(request,'store/product.html',context)

class ProductDetail(DetailView):
    model = Product
    template_name='store/product.html'
    context_object_name='product'


def category(request,foo):
    # foo = foo.replace('-',' ')
    
    try:
        category=Category.objects.get(name=foo)
        products = Product.objects.filter(category=category)
        return render(request,'store/category.html',{'products':products,'category':category})
    except:
        messages.success(request,'That category do not exist')

