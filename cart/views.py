from django.shortcuts import render

# Create your views here.

def view_cart(request):
    
    """ A view to return the view the cart """

    return render(request, 'cart/cart.html')