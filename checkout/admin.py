from django.contrib import admin
from .models import Order, OrderItem


class OrderItemAdminInline(admin.TabularInline):
    model = OrderItem
    readonly_fields = ('orderitem_total',)


def make_published(modeladmin, request, queryset):
    queryset.update(status='p')


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderItemAdminInline,)

    readonly_fields = ('order_number', 'date',
                       'delivery_cost', 'order_total',
                       'grand_total', 'original_bag', 'stripe_pid',)

    fields = ('order_number', 'date', 'first_name',
              'last_name', 'email', 'phone', 'country',
              'postcode', 'city', 'address_line_1',
              'address_line_2', 'order_note', 'delivery_cost',
              'order_total', 'grand_total', 'status',
              'original_bag', 'stripe_pid',)

    list_display = ('order_number', 'date', 'full_name',
                    'order_total', 'delivery_cost',
                    'grand_total', 'status', 'order_note',)

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
