from django.contrib import admin
from .models import *


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category', 'quantity', 'brand', 'price', 'date_added']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


class BrandAdmin(admin.ModelAdmin):
    list_display = ["id", "name", 'profile_image']


admin.site.register(Product, ProductAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Category, CategoryAdmin)
