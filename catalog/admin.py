from django.contrib import admin

from .models import CatalogModel


@admin.register(CatalogModel)
class CatalogAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
