from django.shortcuts import render, redirect, get_object_or_404
from main.forms import ProductForm
from main.models import Product
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
import datetime

from django.views.decorators.csrf import csrf_exempt # Assignment 6
from django.views.decorators.http import require_POST # Assignment 6
from django.utils.html import strip_tags # Assignment 6

# Create your views here.
@login_required(login_url='/login')
def show_main(request):
    context = {
        'name': request.user.username,
        'last_login': request.COOKIES.get('last_login'),
        'npm': '2306172325',
        'class' : 'KKI'
    }

    return render(request, "main.html", context)

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == 'POST':
        products = form.save(commit=False)
        products.user = request.user
        products.save()
        return redirect('main:show_main')

    context = {
        'form': form
    }

    return render(request, "create_product.html", context)


@csrf_exempt
@require_POST
def create_product_ajax(request):
    user = request.user
    name = strip_tags(request.POST.get("name"))
    price = request.POST.get("price")
    description = strip_tags(request.POST.get("description"))
    category = strip_tags(request.POST.get("category"))
    stock = request.POST.get("stock")
    rating = request.POST.get("rating")

    new_product = Product(
        user=user,
        name=name,
        price=price,
        description=description,
        category=category,
        stock=stock,
        rating=rating
    )
    new_product.save()

    return HttpResponse(b"CREATED", status=201)

def edit_product(request, id):
    # Get product entry based on id
    product = Product.objects.get(pk = id)

    # Set product entry as an instance of the form
    form = ProductForm(request.POST or None, instance=product)

    if form.is_valid() and request.method == "POST":
        # Save form and return to home page
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_product.html", context)

def delete_product(request, id):
    product = Product.objects.get(pk=id)
    product.delete()
    return redirect('main:show_main')

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your new account has been sucessfully added!')
            return redirect('main:login')
    context = {
        'form':form
        }
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response

        else:
            messages.error(request, 'Invalid username or password. Please try again.')

    else:
        form = AuthenticationForm(request)
    context = {'form': form}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    return redirect('main:login')

def show_xml(request):
    product = Product.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('xml', product), content_type='application/xml')

def show_json(request):
    product = Product.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', product), content_type='application/json')

def show_xml_by_id(request, id):
    product = Product.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('xml', product), content_type='application/xml')

def show_json_by_id(request, id):
    product = Product.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', product), content_type='application/json')