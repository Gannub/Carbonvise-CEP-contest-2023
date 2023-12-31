from django.urls import path, include
from carts import views


app_name = 'carts'

urlpatterns = [
    path('', views.cart_view, name='carts'),    
    path('update/', views.UpdateCart, name='update'),    
    path('checkout/', views.cart_checkout, name='checkout'),
    path('purchase_complete/', views.Checkout, name='pur_com'),
]