from django.contrib import admin

from core.models import Category, Contact, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'slug')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'is_featured', 'is_active', 'created_at') # Correct `price` to `price_iqd`
    list_editable = ('is_featured', 'is_active') # Remove `price`
    list_filter = ('category', 'is_featured', 'is_active')
    search_fields = ('name', 'description', 'available_sizes', 'available_colors')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'message')