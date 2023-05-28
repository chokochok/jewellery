from django import template
from productapp.models import Category

register = template.Library()


@register.inclusion_tag('mainapp/menu.html')
def menu(request):
    categories = Category.objects.all()
    return {'categories': categories, 'request': request}
