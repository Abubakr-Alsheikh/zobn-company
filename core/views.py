from django.shortcuts import render


def index(request):
    return render(request, "index.html")

def products(request):
    return render(request, "products.html")

def productDetails(request):
    return render(request, "product_details.html")

def contactUs(request):
    return render(request, "contact_us.html")