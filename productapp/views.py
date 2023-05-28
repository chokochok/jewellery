from django.shortcuts import render, get_object_or_404, redirect
from productapp.models import Product, Category, Order, OrderItem
from django.db.models import Q
from .cart import Cart
from django.contrib.auth.decorators import login_required
from .forms import OrderForm


def add_to_cart(request, product_id):
    cart = Cart(request)
    cart.add(product_id=product_id)
    return redirect('cart_view')


def change_quantity(request, product_id):
    action = request.GET.get('action')
    product_id = str(product_id)

    if action:
        quantity = 1
        if action == 'decrease':
            quantity = -1
        cart = Cart(request)
        cart.add(product_id=product_id, quantity=quantity, update_quantity=True)

    return redirect('cart_view')


def remove_from_cart(request, product_id):
    cart = Cart(request)
    cart.remove(product_id=product_id)
    return redirect('cart_view')


def cart_view(request):
    cart = Cart(request)
    return render(request, 'productapp/cart_view.html', {'title': 'Cart', 'cart': cart})


@login_required
def checkout(request):
    cart = Cart(request)

    if cart.get_total_cost() <= 0:
        return redirect('cart_view')

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.total = cart.get_total_cost()
            order.save()

            for item in cart:
                product = item['product']
                quantity = item['quantity']
                price = item['product'].price * quantity
                OrderItem.objects.create(order=order, product=product, quantity=quantity, price=price)

            cart.clear()
            return redirect('my_account')
    else:
        form = OrderForm()
    return render(request, 'productapp/checkout.html', {'title': 'Checkout', 'cart': cart, 'form': form})


def category_detail(request, slug):
    if slug == 'all':
        products = Product.objects.all()
        return render(request, 'productapp/category_detail.html', {'title': 'All products', 'products': products})
    category = get_object_or_404(Category, slug=slug)
    products = category.products.all()
    return render(request, 'productapp/category_detail.html',
                  {'title': category.name, 'category': category, 'products': products})


def product_detail(request, category_slug, slug):
    product = get_object_or_404(Product, slug=slug)
    related_products = Product.objects.filter(category__slug=category_slug).exclude(slug=slug)[:4]
    return render(request, 'productapp/product_detail.html',
                  {'title': product.name, 'product': product, 'related_products': related_products})
