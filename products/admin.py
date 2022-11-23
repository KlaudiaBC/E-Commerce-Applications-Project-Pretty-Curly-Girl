from django.contrib import admin
from .models import Product, Category
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Product)
class ProductAdmin(SummernoteModelAdmin):
    """
    Customise the Add Product form in the Admin Panel.
    Args: SummernoteModelAdmin (describtions): Add tools for
    editing a text in the text field
    """
    list_display = ('sku', 'name', 'category', 'price', 'image',)
    search_fields = ['name', 'category']
    summernote_fields = ('description', )
    ordering = ('sku',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('friendly_name', 'name',)
