from django.contrib import admin
from .models import ProductImage,ProductReviews,Products,Brand,Category



class ProductImageTabuler(admin.TabularInline):
    model = ProductImage


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageTabuler]
    list_display = ['name','flag','category','price']
    list_filter = ['category','brand']
    search_fields = ['name','category','price']
    delete_selected_confirmation_template =['name']


admin.site.register(Products,ProductAdmin)
admin.site.register(ProductImage)
admin.site.register(ProductReviews)
admin.site.register(Brand)
admin.site.register(Category)


