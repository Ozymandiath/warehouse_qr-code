from django.contrib import admin
from django.contrib.auth import get_user_model

from .models import Product, OrderProduct

User = get_user_model()


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "part_name", "availability")
    list_display_links = ("id", "part_name")
    search_fields = ("id", "part_name", "content")
    ordering = ("pk",)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "is_active")
    list_display_links = ("id", "username")
    search_fields = ("id", "username")


@admin.register(OrderProduct)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "order_id", "user", "availability")
    list_display_links = ("id", "order_id")
    search_fields = ("id", "order_id", "user")
