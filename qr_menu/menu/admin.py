from django.contrib import admin
from .models import Category, Company

# admin.site.register(Category)
admin.site.register(Company)

from django.contrib import admin
from .models import Category, MenuItem

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price')
