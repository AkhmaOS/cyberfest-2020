from django.contrib import admin

from .models import RatingModel


@admin.register(RatingModel)
class RatingAdmin(admin.ModelAdmin):
    list_filter = ('name',)
    list_display = ('name', 'level',)
