from django.shortcuts import render
from productapp.models import Product


# Create your views here.
def index(request):
    products = Product.objects.all()[:6]
    return render(request, 'mainapp/index.html', {'title': 'Home', 'products': products})


def about(request):
    return render(request, 'mainapp/about.html', {'title': 'About'})
