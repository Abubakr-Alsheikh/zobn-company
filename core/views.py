from django.shortcuts import redirect, render

from django.views.generic import ListView, DetailView
from core.forms import ContactForm
from core.models import Category, Product


def home(request):
    """
    Displays the homepage.
    """
    featured_products = Product.objects.filter(
        is_featured=True, is_active=True
    ).order_by("-created_at")[:6]
    context = {
        "featured_products": featured_products,
    }
    return render(request, "home/index.html", context)


class ProductListView(ListView):
    model = Product
    template_name = "home/products.html"
    context_object_name = "products"
    paginate_by = 16  # Display 16 products per page

    def get_queryset(self):
        return Product.objects.filter(is_active=True).order_by("-created_at")


class ProductDetailView(DetailView):
    model = Product
    template_name = "home/product_detail.html"
    context_object_name = "product"

def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home:contact_us')
    else:
        form = ContactForm()
    return render(request, 'home/contact_us.html', {'form': form})

def product_care_guides(request):
    return render(request, "home/product_care_guides.html")


def fashion_consultations(request):
    return render(request, "home/fashion_consultations.html")
