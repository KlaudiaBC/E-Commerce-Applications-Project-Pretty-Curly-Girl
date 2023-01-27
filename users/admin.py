from django.contrib import admin
from .models import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = (
                    'user',
                    'default_phone',
                    'default_address_line_1',
                    'default_address_line_2',
                    'default_postcode',
                    'default_city',
                    'default_country',
                    'birthdate')
