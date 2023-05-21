from django.shortcuts import render, get_object_or_404
from productapp.models import Product, Category


def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = category.products.all()
    return render(request, 'productapp/category_detail.html', {'title': category.name, 'category': category, 'products': products})


def product_detail(request, category_slug, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'productapp/product_detail.html', {'title': product.name, 'product': product})
