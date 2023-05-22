from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import UserProfile
from django.contrib.auth.decorators import login_required
from productapp.forms import ProductForm
from django.utils.text import slugify
from productapp.models import OrderItem, Order


def vendor_detail(request, pk):
    user = User.objects.get(pk=pk)
    products = user.products.all()
    return render(request, 'userapp/vendor_detail.html', {'title': 'User Profile', 'user': user, 'products': products})


@login_required
def my_store(request):
    if not request.user.userprofile.is_vendor:
        return redirect('index')
    product = request.user.products.all()
    order_items = OrderItem.objects.filter(product__user=request.user)
    return render(request, 'userapp/my_store.html',
                  {'title': 'My Store', 'products': product, 'order_items': order_items})


@login_required
def add_product(request):
    if not request.user.userprofile.is_vendor:
        return redirect('index')
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.slug = slugify(product.name)
            product.save()
            return redirect('my_store')
    else:
        form = ProductForm()
    return render(request, 'userapp/product_form.html', {'title': 'Add Product', 'form': form})


@login_required
def edit_product(request, pk):
    if not request.user.userprofile.is_vendor:
        return redirect('index')
    product = request.user.products.get(pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            product = form.save(commit=False)
            product.slug = slugify(product.name)
            product.save()
            return redirect('my_store')
    else:
        form = ProductForm(instance=product)
    return render(request, 'userapp/product_form.html', {'title': 'Edit Product', 'form': form, 'product': product})


@login_required
def delete_product(request, pk):
    if not request.user.userprofile.is_vendor:
        return redirect('index')
    product = request.user.products.get(pk=pk)
    product.delete()
    return redirect('my_store')


@login_required
def my_account(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'userapp/my_account.html', {'title': 'My Account', 'orders': orders})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            userprofile = UserProfile.objects.create(user=user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'userapp/signup.html', {'title': 'Sign Up', 'form': form})
