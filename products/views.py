from django.shortcuts import render, get_object_or_404
from .models import Product
from django.db.models import Q

# Create your views here.

def products_list(request):
    """ A view to show all products """

    products = Product.objects.all()
    query = None

    if request.GET:
        if 'search' in request.GET:
            query = request.GET['search']
            products = products.filter(Q(name__icontains=query) | Q(description__icontains=query))

    context = {
        'products': products,
        'search_term': query,
    }    

    return render(request, 'products/products.html', context)

def product_detail(request, product_id):

    """ A view to show individual product page """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }    

    return render(request, 'products/product_detail.html', context)

