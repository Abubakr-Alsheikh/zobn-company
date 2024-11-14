from django.db import models
from django.urls import reverse
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home:category_detail', args=[self.slug])


class Product(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='product_images/', blank=True)
    price_iqd = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Price (IQD)", blank=True, null=True)
    price_aed = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Price (AED)", blank=True, null=True)
    available_sizes = models.CharField(max_length=255, blank=True, verbose_name="Available Sizes")
    available_colors = models.CharField(max_length=255, blank=True, verbose_name="Available Colors")
    processing_time = models.CharField(max_length=255, blank=True, verbose_name="Processing Time")
    is_featured = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_at',)
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name, allow_unicode=True)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('home:product_detail', kwargs={'slug': self.slug})

class Contact(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)  # Assuming phone number is a string
    message = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)  # Add ForeignKey
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)