from django.shortcuts import render

# Create your views here.

def cart_page(request):
    
    """ A view to render the cart page """

    return render(request, 'cart/cart.html')