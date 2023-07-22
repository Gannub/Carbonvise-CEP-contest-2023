from django.shortcuts import render
from carts.models import Cart,CartItem, CartItemHistory
from market.models import Market
import json
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from django.http import JsonResponse
from profiles.models import Profile, CreditSession
from profiles.views import start_session


# Create your views here.
#i am using a function based.
def cart_view(request):
    
    if request.user.is_authenticated:
        
        customer = request.user
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
    print(data)
    deal_slug = data['deal_slug']
    action = data['action']
    print(deal_slug,action)

    customer = request.user
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




@login_required
def TempCheckout(request):
    try:
        user_session = CreditSession.objects.get(user = request.user)
    except CreditSession.DoesNotExist:
        return redirect('howto')

    if user_session.session_active:
        cart_items = CartItem.objects.filter(in_cart=request.user.cart)

        for cart_item in cart_items:
            deal = cart_item.deal
            if deal.quantity_left >= cart_item.quantity:
                deal.quantity_left -= cart_item.quantity
                deal.save()

                #update user credits in the session

                credit_to_add = cart_item.quantity
                user_credit,created = CreditSession.objects.get_or_create(user=request.user)
                # print(user_credit.user_credit)
                user_credit.credits += credit_to_add
                user_credit.save()
                CartItemHistory.objects.create(user=request.user, deal=cart_item.deal,quantity=cart_item.quantity,date_dealed=cart_item.date_added) # add in_session_name later
                
                cart_item.delete()
        
        # print(profile_slug)
        user_cart = request.user.cart
        user_cart.delete()
        






        
        return redirect('index')

    else:
        pass
    # it should redirect to the session educator page (tell users that they have to create a session first )
    # did that using try/except