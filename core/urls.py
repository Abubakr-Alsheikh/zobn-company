from django.urls import path
from .views import contactUs, index, productDetails, products

urlpatterns = [
    path("", index, name="index"),
    path("products", products, name="products"),
    path("product-details", productDetails, name="product-details"),
    path("contact-us", contactUs, name="contact-us"),
]
