from django.shortcuts import render
from products.models import Product, Comments

# Create your views here.

def main(request):
    if request.method == 'GET':
        return render(request, 'layouts/index.html')


def product_view(request):
    if request.method == 'GET':
        products = Product.objects.all()

        context = {
            'products': products
        }


        return render(request, 'products/products.html', context=context)


def product_detal_view(request, id):
    if request.method == 'GET':
        print(id)
        products_obj = Product.objects.get(id=id)
        comments = Comments.objects

        context = {
            'products': products_obj,
            'comments': comments,
        }

        return render(request, 'products/detal.html', context=context)
