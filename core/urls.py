from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from core import views

app_name= "home"
urlpatterns = [
    path("", views.home, name="index"),
    path('about-us/', views.home, name='about_us'),
    path("products", views.ProductListView.as_view(), name="products"),
    path('product-detail/<slug:slug>/', views.ProductDetailView.as_view(), name='product_detail'),
    path(r'^product-detail/(?P<slug>[-\w]+)/$', views.ProductDetailView.as_view(), name='product_detail'),
    path("contact-us", views.contact_us, name="contact_us"),
    path('<slug:slug>/contact-us/', views.contact_us, name='product_contact_us'),
    path(r'^(?P<slug>[-\w]+)/contact-us/$', views.contact_us, name='product_contact_us'),
    path('product-care-guides/', views.product_care_guides, name='product_care_guides'),
    path('fashion-consultations/', views.fashion_consultations, name='fashion_consultations'),
    # dashbaord
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/products/', views.product_list, name='product_list'),
    path('dashboard/products/create/', views.product_create, name='product_create'),
    path('dashboard/products/<int:product_id>/edit/', views.product_edit, name='product_edit'),
    path('dashboard/products/<int:product_id>/delete/', views.product_delete, name='product_delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
