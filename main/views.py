from django.shortcuts import render, redirect
from main.forms import ProductForm
from main.models import Product
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_main(request):
    products = Product.objects.all()
    context = {
        'npm' : '2306172325',
        'name': 'Andriyo Averill Fahrezi',
        'class': 'KKI',
        'products': products
    }

    return render(request, "main.html", context)

def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('main:show_main')
    else :
        form = ProductForm()

    context = {
        'form': form
    }

    return render(request, "create_product.html", context)

def show_xml(request):
    product = Product.objects.all()
    return HttpResponse(serializers.serialize('xml', product), content_type='application/xml')

def show_json(request):
    product = Product.objects.all()
    return HttpResponse(serializers.serialize('json', product), content_type='application/json')

def show_xml_by_id(request, id):
    product = Product.objects.get(pk=id)
    return HttpResponse(serializers.serialize('xml', [product]), content_type='application/xml')

def show_json_by_id(request, id):
    product = Product.objects.get(pk=id)
    return HttpResponse(serializers.serialize('json', [product]), content_type='application/json')