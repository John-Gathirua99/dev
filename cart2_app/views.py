from django.shortcuts import render,get_object_or_404
from .cart import Cart
from store.models import Product
from django.http import JsonResponse
from django.views.generic import DeleteView,UpdateView

def cart_summary(request):
    cart = Cart(request)

    cart_products = cart.get_products()
    quantities = cart.get_quantities
    context = {'cart_products':cart_products,'quantities':quantities}
    return render(request,'cart2_app/cart_summary.html',context)

def cart_add(request):
    
    cart = Cart(request)  #getting cart
    #test for the post request made




    if request.POST.get('action')=='post':
        product_id = int(request.POST.get('product_id'))
        product_quantity = int(request.POST.get('product_qty'))
        
        product = get_object_or_404(Product,id=product_id)

        cart.add(product=product,quantity=product_quantity)
        cart_quantity = cart.__len__()
        response = JsonResponse({'Quantity': cart_quantity})
        return response

def cart_update(request):
    cart= Cart(request)
    if request.POST.get('action')=='post':
        product_id = int(request.POST.get('product_id'))
        product_quantity = int(request.POST.get('product_qty'))

        cart.update(product=product_id,quantity=product_quantity)
        response = JsonResponse({'qty':product_quantity})
        return response
        

def cart_delete(request):
    cart= Cart(request)
    if request.POST.get('action')=='post':
        product_id = int(request.POST.get('product_id'))
        
        cart.delete(product=product_id)
        response = JsonResponse({'Product':product_id})
        return response
    
# class DeleteProduct()

