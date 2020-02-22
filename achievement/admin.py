from django.contrib import admin

from .models import AchievementModel


@admin.register(AchievementModel)
class AchievementMode(admin.ModelAdmin):
    list_filter = ('name',)
    list_display = ('name', 'kirgu_point',)
