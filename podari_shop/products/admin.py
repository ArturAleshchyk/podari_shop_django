from django.contrib import admin

from products.models import Product
from products.models import Category


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'created_at', 'is_published')
    list_display_links = ('id', 'title',)
    list_editable = ('is_published',)
    search_fields = ('title', )


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
