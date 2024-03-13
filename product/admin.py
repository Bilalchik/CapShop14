from django.contrib import admin
from .models import Product, Brand, Category, Image, Storage, Color


admin.site.register(Product)
admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(Image)
admin.site.register(Storage)
admin.site.register(Color)
