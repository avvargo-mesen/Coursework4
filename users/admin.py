from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin


# Register your models here.
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ["email", "username", "phone", "country", "is_staff"]
    fieldsets  = (
        ("Основная информация", {"fields": ("email", "username", "phone", "country", "avatar")}),
        ("Права доступа", {"fields": ("is_staff", "is_active", "is_superuser", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        ("Создать пользователя", {"fields": ("email", "username", "password1", "password2")}),
    )
    search_fields = ["email", "phone"]
    ordering = ('email',)
