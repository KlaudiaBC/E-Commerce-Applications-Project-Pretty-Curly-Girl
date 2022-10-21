from django.contrib import admin
from .models import Product, Category
from django_summernote.admin import SummernoteModelAdmin


class ProductAdmin(SummernoteModelAdmin):
    """
    Customise the Add Product form in the Admin Panel.
    Args: SummernoteModelAdmin (describtions): Add tools for
    editing a text in the text field
    """
    list_display = ('name', 'category', 'sku', 'extra_info')
    search_fields = ['name', 'category']
    summernote_fields = ('description', )


# Register Product and Category Model
admin.site.register(Product)
admin.site.register(Category)
