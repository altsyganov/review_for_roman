from django.contrib import admin
from .models import Product, Type, Price


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = ('price', 'barcode')
    search_fields = ('name', )



admin.site.register(Type)
admin.site.register(Price)
