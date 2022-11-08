from django.contrib import admin
from .models import Order, OrderProduct


class OrderProductAdminInline(admin.TabularInline):
    model = OrderProduct
    readonly_fields = ('product_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderProductAdminInline,)

    readonly_fields = ('order_number', 'date',
                       'delivery_cost', 'order_total',
                       'grand_total',)

    fields = ('order_number', 'date', 'first_name',
              'last_name', 'email', 'phone', 'country',
              'postcode', 'city', 'address_line_1',
              'address_line_2', 'order_note', 'delivery_cost',
              'order_total', 'grand_total', 'status',)

    list_display = ('order_number', 'date', 'full_name',
                    'order_total', 'delivery_cost',
                    'grand_total', 'status', 'order_note',)

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
