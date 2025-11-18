from django.shortcuts import render, redirect, get_object_or_404
from main.forms import ProductForm
from main.models import Product
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags
import json
import datetime
import requests
import json

# Create your views here.

@login_required(login_url="/login")
def show_main(request):
    # product_list = Product.objects.all()

    filter_type = request.GET.get("filter", "all")  # default 'all'

    if filter_type == "all":
        product_list = Product.objects.all()
    else:
        product_list = Product.objects.filter(user=request.user)

    context = {
        'npm' : '2406405304',
        'name': 'Alfino Ahmad Feriza',
        'class': 'PBP C',
        'product_list' : product_list ,
        'last_login' : request.COOKIES.get('last_login', 'Never')
    }

    return render(request, "main.html", context)

@login_required(login_url="/login")
@csrf_exempt
def create_product(request):
    if request.method == "GET":
        return render(request, "create_product.html")

    elif request.method == "POST":
        try:
            data = json.loads(request.body.decode("utf-8"))
            product = Product.objects.create(
                user=request.user,
                name=data.get("name"),
                brand=data.get("brand"),
                description=data.get("description"),
                category=data.get("category"),
                thumbnail=data.get("thumbnail"),
                price=data.get("price") or 0,
                stock=data.get("stock") or 0,
                is_featured=data.get("is_featured", False),
            )
            return JsonResponse({
                "success": True,
                "message": "Product created successfully",
                "id": str(product.id),
            })
        except Exception as e:
            return JsonResponse({
                "success": False,
                "message": str(e),
            }, status=400)

    return JsonResponse({"success": False, "message": "Invalid request"}, status=405)

def show_product(request, id):
    product = get_object_or_404(Product, pk=id)

    context = {
        'product': product
    }
    return render(request, "product_detail.html", context)

def show_xml(request):
     product_list = Product.objects.all()
     xml_data = serializers.serialize("xml", product_list)
     return HttpResponse(xml_data, content_type="application/xml")

def show_json(request):
    product_list = Product.objects.all()
    
    data = [
        {
            'id': str(product.id),
            'name': product.name,
            'brand': product.brand,
            'description': product.description,
            'category': product.category,
            'category_display': product.get_category_display(), 
            'thumbnail': product.thumbnail,
            'price': product.price,
            'stock' : product.stock,
            'is_featured': product.is_featured,
            'user_id': product.user_id,
        }
        for product in product_list
    ]

    return JsonResponse(data, safe=False)

def show_xml_by_id(request, product_id):
   try:
    product_item = Product.objects.filter(pk=product_id)
    xml_data = serializers.serialize("xml", product_item)
    return HttpResponse(xml_data, content_type="application/xml")
   except Product.DoesNotExist:
       return HttpResponse(status=404)

def show_json_by_id(request, product_id):
    try:
        product = Product.objects.select_related('user').get(pk=product_id)
        data = {
            'id': str(product.id),
            'name': product.name,
            'brand': product.brand,
            'description': product.description,
            'category': product.category,
            'category_display': product.get_category_display(), 
            'thumbnail': product.thumbnail,
            'price': product.price,
            'stock' : product.stock,
            'is_featured': product.is_featured,
            'user_id': product.user_id,
            'user_username': product.user.username if product.user_id else None,
        }
        return JsonResponse(data)
    except Product.DoesNotExist:
        return JsonResponse({'detail': 'Not found'}, status=404)

@csrf_exempt
def register(request):
    if request.method == "GET":
        return render(request, "register.html")

    elif request.method == "POST":
        if request.headers.get("Content-Type") != "application/json":
            return JsonResponse({"success": False, "message": "AJAX only"}, status=400)

        try:
            data = json.loads(request.body.decode("utf-8"))
        except Exception as e:
            return JsonResponse({"success": False, "message": f"Invalid JSON: {e}"}, status=400)

        form = UserCreationForm(data={
            "username": data.get("username", ""),
            "password1": data.get("password1", ""),
            "password2": data.get("password2", ""),
        })

        if form.is_valid():
            form.save()
            return JsonResponse({"success": True, "message": "Account created"})

        return JsonResponse({
            "success": False,
            "errors": form.errors
        }, status=400)

    return JsonResponse({"success": False, "message": "Method not allowed"}, status=405)

@csrf_exempt
def login_user(request):
    if request.method == 'GET':
        return render(request, 'login.html')

    elif request.method == 'POST':
        if request.headers.get('Content-Type') == 'application/json':
            try:
                data = json.loads(request.body.decode('utf-8'))
                username = data.get('username')
                password = data.get('password')

                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    response = JsonResponse({"success": True, "message": "Login successful"})
                    response.set_cookie('last_login', str(datetime.datetime.now()))
                    return response
                else:
                    return JsonResponse({"success": False, "message": "Invalid username or password"}, status=401)
            except Exception as e:
                return JsonResponse({"success": False, "message": str(e)}, status=400)
            
    return JsonResponse({"success": False, "message": "Invalid request"}, status=405)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse("main:login"))
    response.delete_cookie('last_login')
    return response

@csrf_exempt
def edit_product(request, id):
    product = get_object_or_404(Product, pk=id, user=request.user)

    if request.method == "GET":
        # render halaman edit product dengan data awal
        return render(request, "edit_product.html", {"product": product})

    elif request.method == "POST":
        if request.headers.get("Content-Type") != "application/json":
            return JsonResponse({"success": False, "message": "AJAX only"}, status=400)

        try:
            data = json.loads(request.body.decode("utf-8"))

            product.name = strip_tags(data.get("name", product.name))
            product.brand = data.get("brand", product.brand)
            product.description = strip_tags(data.get("description", product.description))
            product.category = data.get("category", product.category)
            product.thumbnail = data.get("thumbnail", product.thumbnail)
            product.price = data.get("price") or 0
            product.stock = data.get("stock") or 0
            product.is_featured = data.get("is_featured", False)
            product.save()

            return JsonResponse({
                "success": True,
                "message": "Product updated successfully",
                "id": str(product.id),
            })
        except Exception as e:
            return JsonResponse({
                "success": False,
                "message": str(e),
            }, status=400)

    return JsonResponse({"success": False, "message": "Invalid request"}, status=405)

def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

def product_list_by_category(request, category=None):
    products = Product.objects.all()

    if category == "apparels":
        products = products.filter(category__in=["Shirts", "Hoodies", "Socks", "Shorts"])
    elif category == "shoes":
        products = products.filter(category="Shoes")
    elif category == "others":
        products = products.filter(category="Ball")

    # extra filter
    filter_type = request.GET.get("filter")
    if filter_type == "my" and request.user.is_authenticated:
        products = products.filter(user=request.user)

    context = {
        'npm' : '2406405304',
        'name': 'Alfino Ahmad Feriza',
        'class': 'PBP C',
        "products": products,
        "category": category,
        "last_login": request.COOKIES.get('last_login', 'Never')
    }

    return render(request, "product_list.html", context)

@csrf_exempt
@require_POST
def add_product_ajax(request):
    """
    Handle AJAX form submission to create a new Product.
    Works with both form-data and JSON-based requests.
    """
    try:
        if request.content_type == 'application/json':
            import json
            data = json.loads(request.body.decode('utf-8'))
        else:
            data = request.POST

        raw_name = data.get("name")
        brand = data.get("brand")
        raw_description = data.get("description")
        category = data.get("category")
        thumbnail = data.get("thumbnail")
        price = data.get("price") or 0
        stock = data.get("stock") or 0
        is_featured = (
            str(data.get("is_featured")).lower() in ["true", "on", "1"]
        )
        user = request.user if request.user.is_authenticated else None

        name = strip_tags(raw_name)
        description = strip_tags(raw_description)

        # Basic validation
        if not name or not category:
            return JsonResponse({
                "success": False,
                "message": "Product name and category are required."
            }, status=400)

        # Save product
        new_product = Product.objects.create(
            user=user,
            name=name,
            brand=brand,
            description=description,
            category=category,
            thumbnail=thumbnail,
            price=price,
            stock=stock,
            is_featured=is_featured,
        )

        return JsonResponse({
            "success": True,
            "message": "Product created successfully.",
            "id": str(new_product.id),
        }, status=201)

    except Exception as e:
        return JsonResponse({
            "success": False,
            "message": f"Error: {str(e)}"
        }, status=500)
    
def proxy_image(request):
    image_url = request.GET.get('url')
    if not image_url:
        return HttpResponse('No URL provided', status=400)
    
    try:
        # Fetch image from external source
        response = requests.get(image_url, timeout=10)
        response.raise_for_status()
        
        # Return the image with proper content type
        return HttpResponse(
            response.content,
            content_type=response.headers.get('Content-Type', 'image/jpeg')
        )
    except requests.RequestException as e:
        return HttpResponse(f'Error fetching image: {str(e)}', status=500)
    
@csrf_exempt
def create_product_flutter(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        name = strip_tags(data.get("name", ""))
        brand = strip_tags(data.get("brand", ""))
        description = strip_tags(data.get("description", ""))
        category = strip_tags(data.get("category", ""))
        thumbnail = data.get("thumbnail", "")
        price = data.get("price", 0)
        stock = data.get("stock", 0)
        is_featured = data.get("is_featured", False)

        try:
            product = Product.objects.create(
                name=name,
                brand=brand,
                description=description,
                category=category,
                thumbnail=thumbnail,
                price=price,
                stock=stock,
                is_featured=is_featured,
                user=request.user if request.user.is_authenticated else None,
            )

            return JsonResponse({
                "status": "success",
                "message": "Product created successfully",
                "id": str(product.id),
            })

        except Exception as e:
            return JsonResponse({
                "status": "error",
                "message": str(e)
            }, status=500)

    return JsonResponse({
        "status": "error",
        "message": "Invalid request method"
    }, status=400)


def show_json_my_products(request):
    product_list = Product.objects.all().filter(user=request.user)
    data = [
        {
            'id': str(product.id),
            'name': product.name,
            'brand': product.brand,
            'description': product.description,
            'category': product.category,
            'category_display': product.get_category_display(), 
            'thumbnail': product.thumbnail,
            'price': product.price,
            'stock' : product.stock,
            'is_featured': product.is_featured,
            'user_id': product.user_id,
        }
        for product in product_list
    ]

    return JsonResponse(data, safe=False)




    






 








