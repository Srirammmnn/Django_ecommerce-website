# Create your views here.
from django.shortcuts import render,get_object_or_404
from django.contrib import messages
from .cart import Cart
from django_app.models import Product
from django.http import JsonResponse
from django.shortcuts import redirect


def cart_summary(request):
    cart= Cart(request)
    cart_products = cart.get_prods
    quantities = cart.get_quants
    totals = cart.cart_total()
    return render(request, "cart_summary.html", {"cart_products":cart_products, "quantities":quantities,"totals":totals})
    

def cart_add(request):   
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))

        product = get_object_or_404(Product, id=product_id)
        
        cart.add(product=product, quantity=product_qty)
        cart_quantity = cart.__len__()
        response=JsonResponse({'qty': cart_quantity})
        messages.success(request, ("product addedto cart"))
        return response
        
def cart_update(request):
    cart = Cart(request)

    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))
        cart.update(product=product_id,quantity=product_qty)
        response = JsonResponse({'qty':product_qty})
        messages.success(request, ("your cart has been updated....."))
        return response

def cart_delete(request):
    cart = Cart(request)

    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
      
        cart.delete(product=product_id)
        response = JsonResponse({'product':product_id})

        messages.success(request, ("Item has been deleted....."))
        return response

def cart_item_count(request):
    cart = Cart(request)
    return {
        'cart_quantity': len(cart)
    }

def cart_buy(request):
    return render(request,'buy.html',{})

from django.shortcuts import render

def order_confirmation(request):
    cart = request.session.get('cart', {})  # Or your cart logic
    cart_products = []
    total = 0

    for product_id, quantity in cart.items():
        try:
            product = Product.objects.get(id=product_id)
            product.quantity = quantity  # optional if you want to display quantity
            product.total_price = quantity * (product.sale_price or product.price)
            total += product.total_price
            cart_products.append(product)
        except Product.DoesNotExist:
            continue

    context = {
        'cart_products': cart_products,
        'totals': total
    }
    return render(request, 'order_confirmation.html', context)

