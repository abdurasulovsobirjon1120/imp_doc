from django.contrib import admin
from .models import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('phone_number', 'email', 'first_name', 'last_name')
        }),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')
        }),
    )

    list_display = ('phone_number', 'email', 'first_name', 'last_name', 'is_active', 'is_staff')
    search_fields = ('phone_number', 'email', 'first_name', 'last_name')

admin.site.register(CustomUser, CustomUserAdmin)