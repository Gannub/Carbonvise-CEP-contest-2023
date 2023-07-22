from django.contrib import admin

# Register your models here.
from carts.models import Cart, CartItem, CartItemHistory


admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(CartItemHistory)


