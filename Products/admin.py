from django.contrib import admin

# Register your models here.
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'weight', 'price', 'created_at','updated_at')
    list_display_links = (['name'])
    list_filter = ('name', 'weight', 'price','created_at','updated_at')
    search_fields = ('name',)
    list_per_page = 25


admin.site.register(Product, ProductAdmin)

