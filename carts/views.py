from django.shortcuts import render
from carts.models import Cart,CartItem
from market.models import Market
import json
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
# Create your views here.
#i am using a function based.
def cart_view(request):
    
    if request.user.is_authenticated:
        
        customer = request.user.profile
        # print(customer.cart.)
        cart,created = Cart.objects.get_or_create(customer=customer, deal_complete=False)
        ## child object (lowercase)_set
        deals = cart.cartitem_set.all()
    else:
       
        deals=[]
        cart = {'cart_item_total':0, 'cart_total':0} 
        return redirect('account_login')
    
    ctx = {'deals':deals, 'cart':cart }
    return render (request,'carts/carts.html',ctx)


def UpdateCart(request):
    data = json.loads(request.body)
    deal_slug = data['deal_slug']
    action = data['action']
    print(deal_slug,action)

    customer = request.user.profile
    deal = Market.objects.get(slug=deal_slug)
    cart,created = Cart.objects.get_or_create(customer=customer, deal_complete=False)
    cart_item ,created = CartItem.objects.get_or_create(in_cart=cart, deal=deal)

    if action == 'add':
        cart_item.quantity+=1
    elif action == 'remove':
       cart_item.quantity-=1 

    cart_item.save()

    if cart_item.quantity <=0:
        cart_item.delete()

    return JsonResponse('deal was updated', safe=False)

    
    
    # return JsonResponse("Deal addded to the cart", safe=False)