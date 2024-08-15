from django.contrib import admin

from catalog.models import Category, Product, Version
from users.models import User


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category')
    list_filter = ('category',)
    search_fields = ('name', 'description',)


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('product', 'version', 'sign_version',)
    list_filter = ('sign_version', 'product', 'version',)
    search_fields = ('product', 'sign_version',)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'is_staff')
    list_filter = ('is_staff',)
    search_fields = ('email',)
