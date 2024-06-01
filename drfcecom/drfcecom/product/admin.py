from django.contrib import admin

# Register your models here.
from .models import Brand, Product, Category, ProductLine

admin.site.register(Product)
admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(ProductLine)
