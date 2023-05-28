from django.shortcuts import render
from productapp.models import Product


# Create your views here.
def index(request):
    # Select last 8 products by date
    products = Product.objects.all().order_by('-created')[:8]
    categories = [product.category for product in products]
    # drop duplicates
    categories = list(set(categories))
    return render(request, 'mainapp/index.html', {'title': 'Jewellery', 'products': products, 'categories': categories})


def about(request):
    return render(request, 'mainapp/about.html', {'title': 'About'})
