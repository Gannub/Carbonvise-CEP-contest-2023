from django.shortcuts import render
from billings.omise_keys import OMISE_PUB_KEY, OMISE_SEC_KEY
from django.http import JsonResponse
from billings.models import BillingProfile
from django.contrib.auth.decorators import login_required
import omise
import json
from cards.models import Card


omise.api_secret = OMISE_SEC_KEY

# Create your views here.
def omise_view(request):
    if request.method == 'POST':

        print('post', request.POST)
    ctx = {
        'pub_key':OMISE_PUB_KEY
    }

    return render(request, 'billings/omise_view.html', ctx)



@login_required
def omise_processor(request):
    # print(request.body)
    token = json.loads(request.body)
    # print('this is token', token)
    billing_profile, created = BillingProfile.objects.get_or_new(request)

    customer = omise.Customer.retrieve(billing_profile.customer_id)
    print('Omise Customer' , customer)
    card = customer.update(card=token)
    # print(card.__dict__)
    cards = customer.cards

    for card in cards:
        # print('########\n', card)
        card_obj, created = Card.objects.get_or_new(request=request, billing_profile=billing_profile, card=card)

    return JsonResponse({'status':'success'})