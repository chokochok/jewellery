from django import forms
from .models import Product, Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('first_name', 'last_name', 'email', 'address', 'postal_code', 'city',)


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'category', 'price', 'description', 'image',)
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full p-4 border border-gray-200'
            }),
            'category': forms.Select(attrs={
                'class': 'w-full p-4 border border-gray-200'
            }),
            'price': forms.NumberInput(attrs={
                'class': 'w-full p-4 border border-gray-200'
            }),
            'description': forms.Textarea(attrs={
                'class': 'w-full p-4 border border-gray-200'
            }),
            'image': forms.FileInput(attrs={
                'class': 'w-full p-4 border border-gray-200'
            }),
        }
