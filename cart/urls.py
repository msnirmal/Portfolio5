from django.urls import path
from .import views

urlpatterns = [
    path('', views.cart_page, name='cart_page'),
    path('add/<item_id>/',views.add_to_cart, name='add_to_cart'),
]


