from django.urls import path, include
from billings import views


app_name = 'carts'

urlpatterns = [
    path('omise_view', views.omise_view, name='omise'),    
    path('omise_processor', views.omise_processor, name='omise_processor'),    
    # path('', views.UpdateCart, name='update'),    
    # path('checkout/', views.TempCheckout, name='checkout'),
]