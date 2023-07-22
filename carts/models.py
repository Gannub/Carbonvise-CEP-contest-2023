from django.db import models
from django.db.models.signals import pre_save
from carts.utils import check_slug_unique
from market.models import Market
from django.contrib.auth import get_user_model
from profiles.models import Profile, CreditSession, CreditHistory

User = get_user_model()

def upload_path(instance, filename):
    return f'item_qr/{filename}'
# Create your models here.
class Cart(models.Model):
    customer = models.OneToOneField(User,on_delete=models.SET_NULL, null=True, blank=True)
    date_dealed = models.DateTimeField(auto_now_add=True)
    deal_complete = models.BooleanField(default=False, null=True, blank=False) #Basically i didnt use this one
    slug = models.SlugField(unique=True,null=True,blank=True)
    
    def __str__(self) -> str:
        return f'{self.customer}'
    
    @property
    def cart_total(self):
        cart_items = self.cartitem_set.all()
        total = sum([item.get_total for item in cart_items])
        return total
    @property
    def cart_item_total(self):
        cart_items = self.cartitem_set.all()
        total = sum([item.quantity for item in cart_items])
        return total
    


class CartItem(models.Model):
    deal = models.ForeignKey(Market, on_delete=models.CASCADE, null=True, blank=True)
    in_cart = models.ForeignKey(Cart, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField(default=0,null=True,blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    # qrcode = models.ImageField(null=True,blank=True,upload_to= upload_path)

    def __str__(self) -> str:
        return f'{self.in_cart} {self.deal} {self.quantity}'

    @property
    def get_total(self):
        total = self.deal.price_per_unit * self.quantity
        return total



def pre_save_slug_field(sender, instance, *arg ,**kwargs):  # sent at the beginning of a model’s save() 
        if not instance.slug:
            instance.slug = check_slug_unique(instance)

pre_save.connect(pre_save_slug_field, sender=Cart)

    

    
def upload_path_history(instance, filename):
    return f'item_qr/{filename}'


class CartItemHistory(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, null=True, blank=True)
    deal = models.ForeignKey(Market, on_delete=models.SET_NULL, null=True, blank=True)
    # in_cart = models.ForeignKey(CartHistory, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField(default=0,null=True,blank=True)
    date_dealed = models.DateTimeField(auto_now_add=False, null=True,blank=True)
    in_session_name = models.CharField(max_length=100, null=True, blank=True)
    qrcode = models.ImageField(null=True,blank=True,upload_to=upload_path_history)


    def __str__(self) -> str:
        return f'{self.user} {self.deal} {self.date_dealed}'
    @property
    def get_total(self):
        total = self.deal.price_per_unit * self.quantity
        return total