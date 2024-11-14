from django.shortcuts import get_object_or_404, redirect, render

from django.views.generic import ListView, DetailView
from core.forms import ContactForm, ProductForm
from core.models import Product
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify


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
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['show_modal'] = len(messages.get_messages(self.request)) > 0
        return context

def contact_us(request, slug=None):
    """
    Handles both general and product-specific contact forms.
    """
    product = None
    print(slug)
    if slug:
        product = get_object_or_404(Product, slug=slug)  # Use get_object_or_404 for better error handling

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)  # Don't save yet
            if product:
                contact.product = product # associate the contact with product
            contact.save() # Now save 
            messages.success(request, 'تم إرسال رسالتك بنجاح!')
            if product:
                return redirect('home:product_detail', slug=product.slug)
            else:
                return redirect('home:contact_us')  # Redirect to the general contact page
    else:
        form = ContactForm()

    context = {'form': form, 'show_modal': len(messages.get_messages(request)) > 0 }  # Check for existing messages from GET request
    if product:
        context['product'] = product

    return render(request, 'home/contact_us.html', context)

def product_care_guides(request):
    return render(request, "home/product_care_guides.html")


def fashion_consultations(request):
    return render(request, "home/fashion_consultations.html")

@login_required
def dashboard(request):
    context = {'user': request.user}
    return render(request, 'dashboard/_dashboard.html', context)

@login_required
def product_list(request):
    products = Product.objects.order_by('-is_active', '-created_at')
    context = {'products': products}
    return render(request, 'dashboard/product_list.html', context)


@login_required
def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            slug = slugify(name, allow_unicode=True)

            if Product.objects.filter(slug=slug).exists():
                messages.error(request, 'اسم المنتج موجود بالفعل. يرجى اختيار اسم مختلف.')
            else:
                form.save()
                messages.success(request, 'تم إنشاء المنتج بنجاح')
                return redirect('home:product_list')
    else:
        form = ProductForm()
    context = {'form': form}
    return render(request, 'dashboard/product_form.html', context)

@login_required
def product_edit(request, product_id):
    product = Product.objects.get(pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            slug = slugify(name, allow_unicode=True)

            if Product.objects.filter(slug=slug).exclude(pk=product_id).exists(): # If it exists, it would be different product since we are excluding the current product id
                messages.error(request, 'اسم المنتج موجود بالفعل. يرجى اختيار اسم مختلف.')
            else:
                form.save() # If it passes, save data
                messages.success(request, 'تم حفظ المنتج بنجاح')
                return redirect('home:product_list')
    else:
        form = ProductForm(instance=product)
    context = {'product': product, 'form': form}
    return render(request, 'dashboard/product_form.html', context)

@login_required
def product_delete(request, product_id):
    product = Product.objects.get(pk=product_id)
    if request.method == 'POST':
        product.delete()
        messages.success(request, 'تم حذف المنتج بنجاح')
        return redirect('home:product_list')
    context = {'product': product}
    return render(request, 'dashboard/product_delete.html', context)