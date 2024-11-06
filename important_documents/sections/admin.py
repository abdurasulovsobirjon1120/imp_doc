from django.contrib import admin
from .models import Section, File  # Section va File modellari import qilinadi
from accounts.models import CustomUser  # CustomUser modelini import qilish

class FileInline(admin.TabularInline):
    model = File
    extra = 1

class CustomUserAdmin(admin.ModelAdmin):
    inlines = [FileInline]  # Foydalanuvchiga bog'liq File yozuvlarini ko‘rsatish
    fieldsets = (
        (None, {
            'fields': ('phone_number', 'email', 'first_name', 'last_name', 'created_at')
        }),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')
        }),
    )
    readonly_fields = ('created_at',)  # 'created_at' faqat o'qiladigan qilib qo‘yiladi
    list_display = ('email', 'phone_number', 'is_staff', 'is_active')  # Ro'yxat ko‘rinishidagi ustunlar
    search_fields = ('email', 'phone_number', 'first_name', 'last_name')  # Qidiruv maydonlari
    ordering = ('email',)  # Tashkil qilish uchun tartib

class SectionAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')  # Section ro'yxat ko'rinishi uchun ustunlar
    search_fields = ('name',)  # Qidiruv maydoni

class FileAdmin(admin.ModelAdmin):
    list_display = ('file_name', 'file_type', 'file_size', 'created_at')  # File ro'yxatidagi ustunlar
    search_fields = ('file_name',)  # Qidiruv maydoni
    readonly_fields = ('created_at', 'file_size')  # 'created_at' va 'file_size' faqat o'qish uchun


admin.site.register(Section, SectionAdmin)
admin.site.register(File, FileAdmin)
