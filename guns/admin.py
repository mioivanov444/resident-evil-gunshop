from django.contrib import admin
from .models import Gun, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name',)


@admin.register(Gun)
class GunAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'game', 'real_life_name')
    list_filter = ('game', 'categories')
    search_fields = ('name', 'real_life_name', 'game')
    filter_horizontal = ('categories',)