from django.contrib import admin
from .models import Product, Category, Review
from django_summernote.admin import SummernoteModelAdmin


@admin.action(description='Mark selected products as on SALE')
def make_sale(modeladmin, request, queryset):
    queryset.update(sale=True)
    obj.save()


@admin.register(Product)
class ProductAdmin(SummernoteModelAdmin):
    """
    Customise the Add Product form in the Admin Panel.
    Args: SummernoteModelAdmin (describtions): Add tools for
    editing a text in the text field
    """
    list_display = ('category', 'sku', 'name', 'price', 'image', 'sale')
    search_fields = ['name', 'category']
    summernote_fields = ('description', )
    ordering = ('sku',)
    actions = [make_sale]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('friendly_name', 'name',)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    """
    Customise the Comment Post form in the Admin Panel.
    """
    list_display = ('author', 'body', 'product', 'created_on')
    list_filter = ('author', 'created_on')
    search_fields = ('author', 'product')
